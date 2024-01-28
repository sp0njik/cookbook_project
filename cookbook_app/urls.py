from django.urls import path

from cookbook_app import views

urlpatterns = [
    path('add_product_to_recipe/', views.add_product_to_recipe, name='add_product_to_recipe'),

]