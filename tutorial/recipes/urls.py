from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tutorial.recipes import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'recipes', views.RecipeViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
