from django.contrib import admin

from cookbook_app.models import Product, Recipe, RecipeProduct

admin.site.register(Product)
admin.site.register(Recipe)
admin.site.register(RecipeProduct)
