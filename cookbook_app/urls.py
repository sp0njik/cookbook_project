from django.urls import path

from cookbook_app import views

urlpatterns = [
    path('show_recipes_without_product/', views.show_recipes_without_product, name='show_recipes_without_product'),
    path('add_product_to_recipe/', views.add_product_to_recipe, name='add_product_to_recipe'),
    path('cook_recipe/', views.cook_recipe, name='cook_recipe'),
]