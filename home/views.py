from django.shortcuts import render, get_object_or_404, redirect
from .models import Subscribe, Newsletter
from .forms import SubscribeForm, NewsLetterForm
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
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


def newsletter(request):
    form = NewsLetterForm()
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            email = form.cleaned_data.get('subscribers').split(',')
            body = form.cleaned_data.get('content')

            mail = EmailMultiAlternatives(subject, body, settings.DEFAULT_FROM_EMAIL, bcc=email)
            mail.content_subtype = 'html'
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

        return redirect('newsletter')
    form.fields["subscribers"].initial = ','.join(
        [active.email for active in Subscribe.objects.all()])
    template = 'newsletter_superuser.html'
    context = {"form": form}

    return render(request, template, context)
