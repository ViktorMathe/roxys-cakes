from django.shortcuts import render, get_object_or_404
from .models import Subscribe
from .forms import SubscribeForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


def home(request):
    return render(request, 'index.html')


def add_subscriber(request):
    form = SubscribeForm()
    if request.method == 'POST':
        post_data = request.POST.copy()
        form = SubscribeForm(request.POST)
        if form.is_valid():
            email = post_data.get('email',)
            form.save()
            email = email
            subject = render_to_string(
                'newsletter_emails/newsletter_confirmation_subject.txt')
            body = render_to_string(
                'newsletter_emails/newsletter_confirmation_body.txt')
            send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [email])
    template = 'newsletter.html'
    context = {'form': form}
    return render(request, template, context)
