from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField

# Create your models here.


class Checkout(models.Model):
    order_number = models.CharField(max_length=32, editable=False, null=False)
    full_name = models.CharField(max_length=64, blank=False, null=False)
    email_address = models.EmailField(max_length=254, blank=False, null=False)
    phone_number = models.CharField(max_length=24, blank=False, null=False)
    city = models.CharField(max_length=50, blank=False, null=False)
    address_1 = models.CharField(max_length=100, blank=False, null=False)
    address_2 = models.CharField(max_length=100, blank=False, null=False)
    county = models.CharField(max_length=50, blank=True, null=True)
    post_code = models.CharField(max_length=50, blank=False, null=False)
    country = CountryField(
        blank_label='Country *', blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    bag_total = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=False)
    delivery = models.DecimalField(
        max_digits=8, decimal_places=2, default=0, null=False)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=False)
    stripe_pid = models.CharField(
        max_length=254, blank=False, null=False, default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()
