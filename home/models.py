from django.db import models
from django_summernote.widgets import SummernoteWidget
import datetime
import uuid


class Subscribe(models.Model):
    email = models.EmailField(unique=True)
    conf_number = models.CharField(max_length=12, null=False, editable=False)
    confirmed = models.BooleanField(default=True)

    def _generate_conf_number(self):
        return uuid.uuid4().hex.upper()

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
