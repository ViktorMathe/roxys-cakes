from django.shortcuts import render, redirect

import stripe

# Create your views here.
stripe.api_key = ''


def create_checkout_session(request):
    session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'T-shirt',
                    },
                    'unit_amount': 2000,
                },
                'quantity': 1,
                }],
            mode='payment',
            success_url='',
            cancel_url='http://localhost:4242/cancel',
        )

    template = 'checkout.html'

    return redirect(session.url, code=303)


def checkout_success(request):
    template = 'checkout_success.html'

    return render(request, template)
