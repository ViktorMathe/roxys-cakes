from django.db import models


# Cakes categories model
class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=150)
    friendly_name = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


# Cakes models
class Cake(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=150)
    description = models.TextField()
    flavours = models.CharField(max_length=50, null=True, blank=True)
    ingredients = models.CharField(max_length=245, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
