from tutorial.recipes.models import Recipe
from tutorial.recipes.serializers import RecipeSerializer
from rest_framework import viewsets


class RecipeViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides CRUD actions.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
