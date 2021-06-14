from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField()





