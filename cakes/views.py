from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Cake, Category
from django.contrib.auth.decorators import login_required
from .forms import CakeForm
from django.contrib import messages

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
        messages.success(request, f'{cake.name} has been added to the database.')
        return redirect('cakes')
    else:
        form = CakeForm()

    template = 'add_cake.html'
    context = {
        'form': form
    }

    return render(request, template, context)


@login_required
def delete_cake(request, cake_id):
    cake = get_object_or_404(Cake, pk=cake_id)
    cake.delete()
    messages.warning(request, f'{cake.name} has been deleted!')
    return redirect(reverse('cakes'))


@login_required
def edit_cake(request, cake_id):
    cake = get_object_or_404(Cake, pk=cake_id)
    if request.method == 'POST':
        form = CakeForm(request.POST, request.FILES, instance=cake)
        if form.is_valid():
            form.save()
            messages.success(request, f'{cake.name} has been updated!')
            return redirect(reverse('cakes'))
    else:
        form = CakeForm(instance=cake)

    template = 'edit_cake.html'
    context = {
        'form': form,
        'cake': cake
    }

    return render(request, template, context)


def cake_details(request, cake_id):
    cake = get_object_or_404(Cake, pk=cake_id)

    template = 'cake_details.html'
    context = {
        'cake': cake
    }
    return render(request, template, context)
