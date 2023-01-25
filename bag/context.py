from django.shortcuts import get_object_or_404
from decimal import Decimal
from django.conf import settings
from cakes.models import Cake


def bag_contents(request):
    bag_contents = []
    total = 0
    cakes = 0
    bag = request.session.get('bag', {})

    for cake_id, quantity in bag.items():
        cake = get_object_or_404(Cake, pk=cake_id)
        total += quantity * cake.price
        cakes += quantity
        bag_contents.append({
            'cake_id': cake_id,
            'quantity': quantity,
            'cake': cake,
        })

    if total < settings.FREE_DELIVERY:
        delivery = total * Decimal(settings.DELIVERY_PERCENTAGE/100)
        free_delivery_delta = settings.FREE_DELIVERY - total
    else:
        delivery = 0
        free_delivery_delta = 0

    order_total = delivery + total

    context = {
        'bag_contents': bag_contents,
        'total': total,
        'cakes': cakes,
        'free_delivery': settings.FREE_DELIVERY,
        'free_delivery_delta': free_delivery_delta,
        'order_total': order_total,
    }

    return context
