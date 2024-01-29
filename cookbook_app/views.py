from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render
from django.db.models import F, Q
from django.db import transaction

from cookbook_app.models import Product, Recipe, RecipeProduct


def add_product_to_recipe(request):
    if request.method == "GET":
        recipe_id = request.GET.get("recipe_id")
        product_id = request.GET.get("product_id")
        weight = request.GET.get("weight")
        if RecipeProduct.objects.filter(
            recipe_id=recipe_id, product_id=product_id
        ).exists():
            recipies_data = RecipeProduct.objects.filter(
                recipe_id=recipe_id, product_id=product_id
            ).select_for_update()
            with transaction.atomic():
                recipies_data.update(weight=F("weight") + int(weight))
        else:
            RecipeProduct.objects.create(
                recipe_id=recipe_id, product_id=product_id, weight=weight
            )
        return HttpResponse(status=200)
    return HttpResponse(status=405)


def cook_recipe(request):
    if request.method == "GET":
        recipe_id = request.GET.get("recipe_id")

    if not recipe_id:
        return HttpResponseBadRequest(status=400)

    products = Product.objects.filter(recipe__id=recipe_id).select_for_update()
    with transaction.atomic():
        products.update(times_cooked=F("times_cooked") + 1)
    return HttpResponse(status=200)


def show_recipes_without_product(request):
    if request.method == "GET":
        product_id = request.GET.get("product_id")
        if not product_id or not Product.objects.filter(id=product_id).exists():
            return HttpResponseBadRequest(status=400)
        recipes = Recipe.objects.only("name").exclude(
            recipeproduct__product__id=product_id, recipeproduct__weight__gte=10
        )
        return render(
            request, "show_recipes_without_product.html", {"recipes": recipes}
        )
    return HttpResponse(status=405)
