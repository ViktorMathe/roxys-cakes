from django.shortcuts import render, get_object_or_404
from .forms import Contact_usForm


def contact_us(request):
    if request.method == 'POST':
        form = Contact_usForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Contact_usForm()
    context = {'form': form}
    return render(request, 'contact_us.html', context)
