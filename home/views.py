from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Subscribe, Newsletter
from .forms import SubscribeForm, NewsLetterForm
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect


def home(request):
    return render(request, 'index.html')


def add_subscriber(request):
    form = SubscribeForm()
    sub_msg = messages.add_message(request, messages.INFO, 'You succesfully subscribed for our newsletter!')
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
            return HttpResponseRedirect(reverse('home'), sub_msg)
    template = 'newsletter.html'
    context = {'form': form}
    return render(request, template, context)


@login_required
def newsletter(request):
    form = NewsLetterForm()
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            to = form.cleaned_data.get('subscribers').split(',')
            body_content = form.cleaned_data.get('content')
            subscribers = Subscribe.objects.filter(confirmed=True)
            for sub in subscribers:
                mail = EmailMultiAlternatives(
                     subject,
                     body_content + (
                        '<br><a href="{}/?email={}">Unsubscribe</a>').format(
                            request.build_absolute_uri('unsubscribe/'),
                            sub.email,),
                     settings.DEFAULT_FROM_EMAIL,
                     bcc=to)
                mail.content_subtype = 'html'
                mail.send()
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

        return redirect('newsletter')
    form.fields["subscribers"].initial = ','.join(
        [active.email for active in Subscribe.objects.all()])
    template = 'newsletter_superuser.html'
    context = {"form": form}

    return render(request, template, context)


def unsubscribe(request):
    sub = Subscribe.objects.get(email=request.GET['email'])
    if sub.email == request.GET['email']:
        sub.delete()
        return render(request, 'index.html', {'email': sub.email})
