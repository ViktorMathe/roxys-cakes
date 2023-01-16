from django.shortcuts import render, redirect
from .models import Cake, Category
from django.contrib.auth.decorators import login_required
from .forms import CakeForm

# Create your views here.


def all_cakes(request):
    cakes = Cake.objects.all()
    categories = None

    if request.GET:
        cakes = cakes
    context = {'cakes': cakes}
    return render(request, 'cakes.html', context)


@login_required
def add_cake(request):
    form = CakeForm(request.POST, request.FILES)
    if form.is_valid():
        cake = form.save()
        return redirect('cakes')
    else:
        form = CakeForm()

    template = 'add_cake.html'
    context = {
        'form': form
    }

    return render(request, template, context)
