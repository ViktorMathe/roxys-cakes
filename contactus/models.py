from django.db import models


class Contact_us(models.Model):
    phone_number = models.CharField(
        max_length=20, null=True, blank=True)
    email = models.EmailField()
    subject = models.CharField(max_length=254)
    message = models.TextField()

    def __str__(self):
        return self.email
