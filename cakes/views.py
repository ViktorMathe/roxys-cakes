from django.shortcuts import render
from .models import Cake, Category

# Create your views here.


def all_cakes(request):
    cakes = Cake.objects.all()
    categories = None

    if request.GET:
        cakes = cakes
    context = {'cakes': cakes}
    return render(request, 'cakes.html', context)
