from django.shortcuts import get_object_or_404
from decimal import Decimal
from django.conf import settings
from cakes.models import Cake


def bag_contents(request):
    bag_contents = []
    total = 0
    cake_count = 0
    bag = request.session.get('bag', {})

    for cake_id, cake_data in bag.items():
        if isinstance(cake_data, int):
            cake = get_object_or_404(Cake, pk=cake_id)
            total += cake_data * cake.price
            cake_count += cake_data
            bag_contents.append({
                'cake_id': cake_id,
                'quantity': cake_data,
                'cake': cake,
            })

    if total < settings.FREE_DELIVERY:
        delivery_fee = total * Decimal(settings.DELIVERY_PERCENTAGE/100)
        free_delivery_delta = settings.FREE_DELIVERY - total
    else:
        delivery_fee = 0
        free_delivery_delta = 0

    order_total = delivery_fee + total

    context = {
        'bag_contents': bag_contents,
        'total': total,
        'cake_count': cake_count,
        'delivery_fee': delivery_fee,
        'free_delivery': settings.FREE_DELIVERY,
        'free_delivery_delta': free_delivery_delta,
        'order_total': order_total,
    }

    return context
