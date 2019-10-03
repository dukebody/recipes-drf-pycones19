from rest_framework import serializers
from tutorial.recipes.models import Recipe, Ingredient

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name']


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, source='ingredient_set', required=False)

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'description', 'ingredients']
