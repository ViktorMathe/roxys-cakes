from django.contrib import admin
from .models import Reviews


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'content', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name']
    actions = ['disapprove_review']

    def disapprove_review(self, request, queryset):
        queryset.update(aprroved=False)
