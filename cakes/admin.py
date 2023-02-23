from django.contrib import admin
from .models import Cake, Category

# Register your models here.


class CakesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Cake, CakesAdmin)
admin.site.register(Category, CategoryAdmin)
