from django.shortcuts import render

from cookbook_app.models import Product, Recipe, RecipeProduct

def add_product_to_recipe(request):
    if request.method == 'GET':
        recipe_id = request.GET.get('recipe_id')
        product_id = request.GET.get('product_id')
        weight = request.GET.get('weight')
        recipe = Recipe.objects.get(id=recipe_id)
        product = Product.objects.get(id=product_id)
        recipe_product = recipe.recipeprodcut_set.filter(product=product).first()
        if recipe_product:
            recipe_product.weight += int(weight)
            recipe_product.save()
        else:
            RecipeProduct.objects.create(recipe=recipe, product=product, weight=weight)   
        
    return render(request, 'add_product_to_recipe.html')