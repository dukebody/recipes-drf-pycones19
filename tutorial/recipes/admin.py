from django.contrib import admin

from tutorial.recipes.models import Recipe, Ingredient


class IngredientInline(admin.StackedInline):
    model = Ingredient


class RecipeAdmin(admin.ModelAdmin):
    fields = ['name', 'description']
    inlines = [IngredientInline]

admin.site.register(Recipe, RecipeAdmin)
