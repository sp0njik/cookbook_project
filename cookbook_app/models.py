from django.db import models




class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название продукта")
    times_cooked: int = models.IntegerField(
        default=0, verbose_name="Количество приготовленных блюд"
    )
    

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name: str = models.CharField(max_length=100, verbose_name="Название рецепта")
    product: Product = models.ManyToManyField(
        Product, verbose_name="Продукты", through="RecipeProduct"
    )

    def __str__(self):
        return self.name 


class RecipeProduct(models.Model):
    recipe: Recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    product: Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    weight: int = models.IntegerField(verbose_name="Вес в граммах")


