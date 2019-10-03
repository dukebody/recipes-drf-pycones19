from django.urls import path
from tutorial.recipes import views

urlpatterns = [
    path('recipes/<int:pk>/', views.recipes_detail),
]
