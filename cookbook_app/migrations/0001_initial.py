# Generated by Django 4.2.7 on 2024-02-02 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название продукта')),
                ('times_cooked', models.IntegerField(default=0, verbose_name='Количество приготовленных блюд')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название рецепта')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField(verbose_name='Вес в граммах')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookbook_app.product')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookbook_app.recipe')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='product',
            field=models.ManyToManyField(through='cookbook_app.RecipeProduct', to='cookbook_app.product', verbose_name='Продукты'),
        ),
    ]