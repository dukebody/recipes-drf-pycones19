from django.urls import path
from tutorial.recipes import views

urlpatterns = [
    path('recipes/', views.recipe_list),
    path('recipes/<int:pk>/', views.recipes_detail),
]
