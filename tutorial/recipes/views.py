from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from tutorial.recipes.models import Recipe
from tutorial.recipes.serializers import RecipeSerializer


def recipes_detail(request, pk):
    try:
        recipe = Recipe.objects.get(pk=pk)
    except Recipe.DoesNotExist:
        return HttpResponse(status=404)

    serializer = RecipeSerializer(recipe)
    return JsonResponse(serializer.data)
