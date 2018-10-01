from rest_framework import serializers
from recipe.models import Recipe, Instructions, Ingredients, RecipeImage, IngredientsTranslations, MainIngredients


class InstructionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Instructions
        fields = ('step', 'image')


class MainIngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainIngredients
        fields = ('id', 'name', 'icon')


class IngredientsSerializer(serializers.ModelSerializer):
    main_ingredient = MainIngredientSerializer()

    class Meta:
        model = Ingredients
        fields = ('id', 'quantity', 'ingredient', 'main_ingredient')


class RecipeImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = RecipeImage
        fields = 'icon',


class IngredientsTranslationSerializer(serializers.ModelSerializer):
    ingredient = MainIngredientSerializer()

    class Meta:
        model = IngredientsTranslations
        fields = ('id', 'name', 'ingredient')


class RecipeSerializer(serializers.ModelSerializer):
    recipes_instructions = InstructionsSerializer(many=True)
    recipes_ingredients = IngredientsSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ('id', 'user', 'title', 'description', 'time', 'servings', 'recipes_instructions',
                  'recipes_ingredients', 'video')

    def create(self, validated_data):
        recipes_ingredients = validated_data.pop('recipes_ingredients')
        recipes_instructions = validated_data.pop('recipes_instructions')
        recipe1 = Recipe.objects.create(**validated_data)
        for recipe2 in recipes_ingredients:
            Ingredients.objects.create(recipe=recipe1, **recipe2)
        for recipe3 in recipes_instructions:
            Instructions.objects.create(recipe=recipe1, **recipe3)
        return recipe1

    def update(self, instance, validated_data):
        instance.title = validated_data['title']
        instance.time = validated_data['time']
        instance.Servings = validated_data['servings']
        recipes_ingredients = validated_data['recipes_ingredients']
        recipes_instructons = validated_data['recipes_instructions']
        instance.description = validated_data['description']
        instance.save()
        ingredient = (instance.recipes_ingredients).all()
        ingredient.delete()
        instruction = (instance.recipes_instructions).all()
        instruction.delete()
        for recipe2 in recipes_ingredients:
            Ingredients.objects.create(recipe=instance, **recipe2)
        for recipe3 in recipes_instructons:
            Instructions.objects.create(recipe=instance, **recipe3)
        return instance

