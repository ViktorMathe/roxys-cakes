from django.contrib import admin
from .models import Subscribe, Newsletter
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(Subscribe)


@admin.register(Newsletter)
class Newsletter(SummernoteModelAdmin):
    summernote_fields = ('content')
