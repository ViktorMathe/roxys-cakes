from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from cakes.models import Cake
from django.contrib import messages


def bag_view(request):
    return render(request, 'bag.html')


def add_bag_content(request, cake_id):
    cake = get_object_or_404(Cake, pk=cake_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if cake_id in list(bag.keys()):
        bag[cake_id] += quantity
    else:
        bag[cake_id] = quantity
        messages.success(request, f'Added {cake.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def change_bag(request, cake_id):
    cake = get_object_or_404(Cake, pk=cake_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[cake_id] = quantity
    else:
        bag.pop(cake_id)

    request.session['bag'] = bag
    return redirect(reverse('bag_view'))


def delete_from_bag(request, cake_id):
    cake = get_object_or_404(Cake, pk=cake_id)
    try:
        bag = request.session.get('bag', {})

        bag.pop(cake_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
