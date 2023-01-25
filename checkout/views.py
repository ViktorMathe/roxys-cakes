from django.shortcuts import render, redirect, reverse
from django.views.decorators.http import require_POST
from django.conf import settings
from .models import Checkout
from .forms import CheckoutForm
from cakes.models import Cake
import json
import stripe


def checkout_session(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    checkout_form = CheckoutForm()

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
            checkout = checkout_form.save(commit=False)
    else:
        bag = request.session.get('bag', {})
        if not bag:
            checkout_form = CheckoutForm()

    template = 'checkout.html'
    context = {
        'checkout_form': checkout_form,
        'stripe_public_key': stripe_public_key,
    }

    return render(request, template, context)
