from django.shortcuts import render, get_object_or_404
from .forms import Contact_usForm
from django.contrib.auth.decorators import login_required
from .models import Contact_us


def contact_us(request):
    if request.method == 'POST':
        form = Contact_usForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Contact_usForm()
    context = {'form': form}
    return render(request, 'contact_us.html', context)


@login_required
def messages(request):
    messages = Contact_us.objects.filter()
    context = {'messages': messages}
    template = 'messages.html'
    return render(request, template, context)
