from decimal import Decimal
from django.conf import settings


def bag_contents(request):
    bag = []
    total = 0
    cakes = 0

    if total < settings.FREE_DELIVERY:
        delivery = total * Decimal(settings.DELIVERY_PERCENTAGE/100)
        free_delivery_delta = settings.FREE_DELIVERY - total
    else:
        delivery = 0
        free_delivery_delta = 0

    order_total = delivery + total

    context = {
        'bag': bag,
        'total': total,
        'cakes': cakes,
        'free_delivery': settings.FREE_DELIVERY,
        'free_delivery_delta': free_delivery_delta,
        'order_total': order_total,
    }

    return context
