from tutorial.recipes.models import Recipe
from tutorial.recipes.serializers import RecipeSerializer
from rest_framework import viewsets


class RecipeViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides CRUD actions.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_queryset(self):
        queryset = Recipe.objects.all()
        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset
