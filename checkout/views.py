from django.shortcuts import render, redirect, reverse, get_object_or_404, \
    HttpResponse
from django.views.decorators.http import require_POST
from django.conf import settings
from .models import Checkout, CheckoutLine
from .forms import CheckoutForm
from cakes.models import Cake
from bag.context import bag_contents
from django.contrib.auth.models import User
import json
import stripe


@require_POST
def cache_checkout_session(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user
        })
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(content=e, status=400)


def checkout_session(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email_address': request.POST['email_address'],
            'phone_number': request.POST['phone_number'],
            'address_1': request.POST['address_1'],
            'address_2': request.POST['address_2'],
            'county': request.POST['county'],
            'city': request.POST['city'],
            'post_code': request.POST['post_code'],
            'country': request.POST['country'],
        }
        checkout_form = CheckoutForm(form_data)
        if checkout_form.is_valid():
            order = checkout_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.save()
            for cake_id, cake_data in bag.items():
                try:
                    cake = Cake.objects.get(id=cake_id)
                    if isinstance(cake_data, int):
                        order_line_item = CheckoutLine(
                            order=order,
                            cake=cake,
                            quantity=cake_data,
                        )
                        order_line_item.save()
                except Cake.DoesNotExist:
                    order.delete()
                    return redirect(reverse('bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(
                reverse('checkout_success', args=[order.order_number]))
    else:
        bag = request.session.get('bag', {})
        checkout_form = CheckoutForm()
        if not bag:
            return redirect(reverse('cakes'))

        current_bag = bag_contents(request)
        total = current_bag['order_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

    template = 'checkout.html'
    context = {
        'checkout_form': checkout_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Checkout, order_number=order_number)

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
