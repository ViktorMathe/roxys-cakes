from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from .models import Checkout, CheckoutLine
from cakes.models import Cake
from profiles.models import Profile
import json
import stripe
import time


class StripeWH_Handler:
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )
        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        order_total = round(stripe_charge.amount / 100, 2)

        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = Profile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = shipping_details.phone
                profile.default_address_1 = shipping_details.address.line1
                profile.default_address_2 = shipping_details.address.line2
                profile.default_city = shipping_details.address.city
                profile.default_post_code = (
                                shipping_details.address.postal_code)
                profile.default_county = shipping_details.address.state
                profile.default_country = shipping_details.address.country
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Checkout.objects.get(
                    full_name__iexact=shipping_details.name,
                    email_address__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    post_code__iexact=shipping_details.address.postal_code,
                    city__iexact=shipping_details.address.city,
                    address_1__iexact=shipping_details.address.line1,
                    address_2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    order_total=order_total,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Checkout.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} status=200')
        else:
            order = None
            try:
                order = Checkout.objects.create(
                    full_name=shipping_details.name,
                    email_address=billing_details.email,
                    phone_number=shipping_details.phone,
                    address_1=shipping_details.address.line1,
                    address_2=shipping_details.address.line2,
                    city=shipping_details.address.city,
                    post_code=shipping_details.address.postal_code,
                    county=shipping_details.address.state,
                    country=shipping_details.address.country,
                    stripe_pid=pid,
                )
                for cake_id, cake_data in json.loads(bag).items():
                    cake = Cake.objects.get(id=cake_id)
                    if isinstance(cake_data, int):
                        order_line_item = CheckoutLine(
                            order=order,
                            cake=cake,
                            quantity=cake_data,
                        )
                        order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        email_to = order.email_address
        subject = render_to_string(
            'confirmation_emails/email_subject.txt',
            {'order': order})
        body = render_to_string(
            'confirmation_emails/email_body.txt',
            {'order': order,
             'contact_email_address': settings.DEFAULT_FROM_EMAIL})
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [email_to]
            )
        print(email_to)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created \
                 order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
