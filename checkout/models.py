from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField
from cakes.models import Cake
from django.contrib.auth.models import User

import uuid

# Create your models here.


class Checkout(models.Model):
    order_number = models.CharField(max_length=32, editable=False, null=False)
    full_name = models.CharField(max_length=64, blank=False, null=False)
    email_address = models.EmailField(max_length=254, blank=False, null=False)
    phone_number = models.CharField(max_length=24, blank=False, null=False)
    city = models.CharField(max_length=50, blank=False, null=False)
    address_1 = models.CharField(max_length=100, blank=False, null=False)
    address_2 = models.CharField(max_length=100, blank=True, null=True)
    county = models.CharField(max_length=50, blank=True, null=True)
    post_code = models.CharField(max_length=50, blank=False, null=False)
    country = CountryField(
        blank_label='Country *', blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    bag_total = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=False)
    delivery = models.DecimalField(
        max_digits=6, decimal_places=2, default=0, null=False)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=False)
    stripe_pid = models.CharField(
        max_length=254, blank=False, null=False, default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        self.bag_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.bag_total < settings.FREE_DELIVERY:
            self.delivery = (
                self.bag_total * settings.DELIVERY_PERCENTAGE / 100)
        else:
            self.delivery = 0
        print(self.delivery)
        print(settings.FREE_DELIVERY)
        self.order_total = self.bag_total + self.delivery
        self.save()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class CheckoutLine(models.Model):
    order = models.ForeignKey(
        Checkout, null=False, blank=False, on_delete=models.CASCADE,
        related_name='lineitems')
    cake = models.ForeignKey(
        Cake, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False,
        editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.cake.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.cake.sku} on order {self.order.order_number}'
