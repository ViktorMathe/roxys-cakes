from django.shortcuts import render, redirect, reverse
from .models import Subscribe
from .forms import SubscribeForm, NewsLetterForm
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect


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
            messages.success(
                request, f'You have succesfully subscribed for our \
                    newsletter on the following email: "{email}"!')

            return HttpResponseRedirect(reverse('home'))
    template = 'newsletter.html'
    context = {'form': form}
    return render(request, template, context)


@login_required
def newsletter(request):
    form = NewsLetterForm()
    subscribers = Subscribe.objects.filter(confirmed=True)
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            body_content = form.cleaned_data.get('content')
            for sub in subscribers:
                mail = EmailMultiAlternatives(
                     subject,
                     body_content + (
                        '<br><a href="{}/?email={}">Unsubscribe</a>').format(
                            request.build_absolute_uri('unsubscribe'),
                            sub.email,),
                     settings.DEFAULT_FROM_EMAIL,
                     bcc=[sub.email])
                mail.content_subtype = 'html'
                mail.send()
                messages.success(
                    request, 'The newsletter has been sent \
                        to all the subscribers!')
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
    try:

        sub = Subscribe.objects.get(email=request.GET['email'])
        if sub.email == request.GET['email']:
            sub.delete()
            messages.warning(
                request, f'You unsubscribed from our newsletter with the \
                    following email: "{sub.email}". Sorry to see you go!')
            return render(request, 'index.html')
    except Exception:
        messages.error(
            request, 'There is no subscriber with this email address!')
        return render(request, 'index.html')
