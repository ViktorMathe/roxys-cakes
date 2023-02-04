from django.contrib import admin
from .models import Contact_us


@admin.register(Contact_us)
class ContactUsAdmin(admin.ModelAdmin):
    readonly_fields = (
        'phone_number', 'email', 'subject', 'message',)
