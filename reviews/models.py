from django.db import models
from django.contrib.auth.models import User
import datetime

STATUS = ((0, "Draft"), (1, "Published"))


class Reviews(models.Model):
    title = models.CharField(max_length=100, unique=True)
    name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='review_post')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    image = models.ImageField('images', blank=True)
    status = models.IntegerField(choices=STATUS, default=1)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
