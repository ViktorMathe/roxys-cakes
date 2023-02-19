from django.shortcuts import render, redirect, get_object_or_404
from .forms import Contact_usForm
from django.contrib.auth.decorators import login_required
from .models import Contact_us
from django.contrib import messages


def contact_us(request):
    if request.method == 'POST':
        form = Contact_usForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your contact form has been submitted! You will get a reply in 48 hours. Thank you!')
            return redirect('contact_us')
    else:
        form = Contact_usForm()
    context = {'form': form}
    return render(request, 'contact_us.html', context)


@login_required
def contact_messages(request):
    contact_messages = Contact_us.objects.filter()
    context = {'contact_messages': contact_messages}
    template = 'messages.html'
    return render(request, template, context)
