from django.contrib import admin

from cookbook_app.models import Product, Recipe, RecipeProduct


# class ProductInline(admin.TabularInline):
#     model = Product # RecipeProduct
#     extra = 1 


# class RecipeAdmin(admin.ModelAdmin):
#     inlines = [ProductInline]
# admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Recipe)
admin.site.register(Product)
admin.site.register(RecipeProduct)

