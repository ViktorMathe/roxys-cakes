from django.contrib import admin
from .models import Checkout, CheckoutLine
# Register your models here.


class CheckoutLineAdmin(admin.TabularInline):
    model = CheckoutLine
    readonly_fields = ('lineitem_total',)


class CheckoutAdmin(admin.ModelAdmin):
    inlines = (CheckoutLineAdmin,)

    readonly_fields = (
        'order_number', 'date', 'delivery', 'bag_total', 'order_total',
                        'stripe_pid')
    fields = ('order_number', 'date', 'full_name', 'phone_number', 'country',
              'post_code', 'city', 'address_1', 'address_2', 'county',
              'bag_total', 'delivery', 'order_total', 'stripe_pid')

    list_display = ('order_number', 'date', 'full_name', 'bag_total',
                    'delivery', 'order_total')

    ordering = ('-date',)


admin.site.register(Checkout, CheckoutAdmin)
