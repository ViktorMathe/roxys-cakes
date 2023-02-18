from django.contrib import admin
from .models import Subscribe, Newsletter
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    fields = ('email', 'confirmed',)


@admin.register(Newsletter)
class Newsletter(SummernoteModelAdmin):
    summernote_fields = ('content')
