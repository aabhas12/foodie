# Generated by Django 2.1.1 on 2018-09-30 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0005_ingredientstranslations_language_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredients',
            name='main_ingredient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='recipe.MainIngredients'),
        ),
    ]
