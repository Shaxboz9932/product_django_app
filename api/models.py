from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='product/%Y/%m/%d/', blank=True, null=True)


    def __str__(self):
        return self.title



