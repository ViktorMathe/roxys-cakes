from django.db import models


class Subscribe(models.Model):
    email = models.EmailField(unique=True)
    confirmed = models.BooleanField(default=True)

    def __str__(self):
        return self.email + "(" + (
            "not" if not self.confirmed else "") + "confirmed)"


class Newsletter(models.Model):
    subscribers = models.CharField(max_length=124)
    subject = models.CharField(max_length=124)
    content = models.CharField(max_length=2000)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject + self.created_on
