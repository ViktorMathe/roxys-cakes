from django.shortcuts import render, redirect, reverse, get_object_or_404, \
    HttpResponse
from django.template.loader import render_to_string
from django.core.mail import send_mail

from django.views.decorators.http import require_POST
from django.conf import settings
from .models import Checkout, CheckoutLine
from .forms import CheckoutForm
from cakes.models import Cake
from bag.context import bag_contents
from django.contrib import messages
from profiles.models import Profile
from profiles.forms import ProfileForm
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
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
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
                    messages.error(request, (
                        "One of the cakes in your bag wasn't \
                             found in our website."
                        "Please contact us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('bag'))

            request.session['save_info'] = 'save_info' in request.POST
            return redirect(
                reverse('checkout_success', args=[order.order_number]))
    else:
        bag = request.session.get('bag', {})
        checkout_form = CheckoutForm()
        if not bag:
            messages.error(request, "There's nothing in your \
                 bag at the moment! Keep shopping!")
            return redirect(reverse('cakes'))

        current_bag = bag_contents(request)
        total = current_bag['order_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = Profile.objects.get(user=request.user)
                checkout_form = CheckoutForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email_address': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'address_1': profile.default_address_1,
                    'address_2': profile.default_address_2,
                    'city': profile.default_city,
                    'post_code': profile.default_post_code,
                    'county': profile.default_county,
                    'country': profile.default_country,
                })
            except Profile.DoesNotExist:
                checkout_form = CheckoutForm()
        else:
            checkout_form = CheckoutForm()

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

    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        order.profile = profile
        order.save()

        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_address_1': order.address_1,
                'default_address_2': order.address_2,
                'default_city': order.city,
                'default_post_code': order.post_code,
                'default_county': order.county,
            }
            profile_form = ProfileForm(profile_data, instance=profile)
            if profile_form.is_valid():
                profile_form.save()

    messages.success(request, f'The Order was Successful! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email_address}.')
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

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
