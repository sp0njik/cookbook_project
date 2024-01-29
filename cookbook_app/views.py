from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render

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
        
    return HttpResponse('Product added to recipe')


def cook_recipe(request):
    if request.method == 'GET':
        recipe_id = request.GET.get('recipe_id')

    if not recipe_id:
        return HttpResponseBadRequest('recipe_id parameter is required')

    recipe = get_object_or_404(Recipe, id=recipe_id)

    for product in recipe.products.all():
        product.times_cooked += 1
        product.save()

    return HttpResponse('Recipe successfully cooked')


def show_recipes_without_product(request):
    if request.method == 'GET':
        product_id = request.GET.get('product_id')
    recipes = Recipe.objects.exclude(recipeproduct__product__id=product_id).exclude(recipeproduct__weight__gte=10)
    return render(request, 'show_recipes_without_product.html', {'recipes': recipes})