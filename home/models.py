from django.db import models


class Subscribe(models.Model):
    email = models.EmailField(unique=True)
    conf_number = models.CharField(max_length=12, null=False, editable=False)
    confirmed = models.BooleanField(default=True)

    def __str__(self):
        return self.email + "(" + (
            "not" if not self.confirmed else "") + "confirmed)"
