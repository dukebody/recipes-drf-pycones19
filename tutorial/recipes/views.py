from tutorial.recipes.models import Recipe
from tutorial.recipes.serializers import RecipeSerializer
from rest_framework import generics


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeList(generics.ListCreateAPIView):
    """
    List all recipes or create new ones.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    