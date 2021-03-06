from rest_framework import serializers
from recipe.models import Recipe, Instructions, Ingredients, RecipeImage, \
    RecipeType, CuisineType
from user.serializers import UserListSerializer


class InstructionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Instructions
        fields = ('step', 'image')


class IngredientsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredients
        fields = ('id', 'quantity', 'ingredient', 'icon')


class RecipeImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = RecipeImage
        fields = 'icon',


class RecipeTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = RecipeType
        fields = ('id', 'name')


class CuisineTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CuisineType
        fields = ('id', 'name')


class RecipeSerializer(serializers.ModelSerializer):
    recipes_instructions = InstructionsSerializer(many=True)
    recipes_ingredients = IngredientsListSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ('id', 'title', 'description', 'time', 'servings', 'recipes_instructions',
                  'recipes_ingredients', 'video')

    def create(self, validated_data):
        request = self.context.get('request')
        recipes_ingredients = validated_data.pop('recipes_ingredients')
        recipes_instructions = validated_data.pop('recipes_instructions')
        recipe1 = Recipe.objects.create(user=request.user, **validated_data)
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
        recipes_instructions = validated_data['recipes_instructions']
        instance.description = validated_data['description']
        instance.save()
        ingredient = instance.recipes_ingredients.all()
        ingredient.delete()
        instruction = instance.recipes_instructions.all()
        instruction.delete()
        for recipe2 in recipes_ingredients:
            Ingredients.objects.create(recipe=instance, **recipe2)
        for recipe3 in recipes_instructions:
            Instructions.objects.create(recipe=instance, **recipe3)
        return instance


class RecipeRetrieveSerializer(serializers.ModelSerializer):
    recipes_instructions = InstructionsSerializer(many=True)
    recipes_ingredients = IngredientsListSerializer(many=True)
    user = UserListSerializer()

    class Meta:
        model = Recipe
        fields = ('id', 'user', 'title', 'description', 'time', 'servings', 'recipes_instructions',
                  'recipes_ingredients', 'video')


class RecipeListSerializer(serializers.ModelSerializer):
    user = UserListSerializer()

    class Meta:
        model = Recipe
        fields = ('id', 'user', 'title', 'description', 'time', 'servings')
