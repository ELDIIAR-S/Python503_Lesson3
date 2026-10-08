from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def str(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )

    def str(self):
        return self.title


class Review(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def str(self):
        return f'{self.product.title} - {self.rating}'


# from django.db import models
#
#
# class Category(models.Model):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name
#
#
# class Product(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField(blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
#
#     def __str__(self):
#         return self.title
#
#
# class Review(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
#     text = models.TextField()
#     stars = models.PositiveSmallIntegerField(default=5)
#
#     def __str__(self):
#         return f'{self.product} - {self.stars}'