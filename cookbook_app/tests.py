from django.test import TestCase
from django.urls import reverse

from cookbook_app.models import Product, Recipe, RecipeProduct


class CookbookAppTests(TestCase):
    def test_add_product_to_recipe_new_product(self):
        recipe = Recipe.objects.create(name="Test recipe")
        product = Product.objects.create(name="Test product")
        url = reverse(
            "add_product_to_recipe"
        )  # предполагается, что у представления есть имя "add_product_to_recipe"
        response = self.client.get(
            url, {"recipe_id": recipe.id, "product_id": product.id, "weight": 100}
        )
        self.assertEqual(response.status_code, 200)

    def test_add_product_to_recipe_new_product_2(self):
        recipe = Recipe.objects.create(name="Test recipe")
        product = Product.objects.create(name="Test product")
        url = reverse(
            "add_product_to_recipe"
        )  # предполагается, что у представления есть имя "add_product_to_recipe"
        response = self.client.get(
            url, {"recipe_id": recipe.id, "product_id": product.id, "weight": 100}
        )
        self.assertTrue(
            RecipeProduct.objects.filter(
                recipe_id=recipe.id, product_id=product.id, weight=100
            ).exists()
    )

    def test_cook_recipe(self):
        url = reverse("cook_recipe")
        response = self.client.get(url, {"recipe_id": 1})
        self.assertEqual(response.status_code, 200)
