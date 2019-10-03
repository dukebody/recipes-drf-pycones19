from rest_framework import serializers
from tutorial.recipes.models import Recipe, Ingredient

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name']


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, required=False)

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'description', 'ingredients']

    def create(self, validated_data):
        # Create a recipe using only “name” and “description” fields in
        # validated_data. Use recipe = Recipe.objects.create(...).
        ingredients_data = validated_data.pop('ingredients', [])
        recipe = super(RecipeSerializer, self).create(validated_data)

        # for each ingredient in the list validated_data[‘ingredients’]
        for ingredient_data in ingredients_data:
        # create a new ingredient. Use Ingredient.objects.create(recipe=recipe, ...).
            Ingredient.objects.create(recipe=recipe, name=ingredient_data['name'])

        return recipe

    def update(self, instance, validated_data):
        # if there is an “ingredients” field in validated_data
        ingredients_data = validated_data.pop('ingredients', None)
        if ingredients_data is not None:
            # delete all ingredients for the recipe instance. Use instance.ingredients.delete().
            instance.ingredients.all().delete()
            for ingredient_data in ingredients_data:
                # create a new ingredient for each ingredient name in the validated_data[“ingredients”] field
                Ingredient.objects.create(recipe=instance, name=ingredient_data['name'])

        instance = super(RecipeSerializer, self).update(instance, validated_data)
        return instance
