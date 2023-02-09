from django.shortcuts import render, get_object_or_404
from .forms import ReviewForm
from .models import Reviews
from django.contrib.auth.decorators import login_required


def reviews(request):
    reviews = Reviews.objects.filter(status=1)
    review = get_object_or_404(reviews)
    context = {'review': review}
    return render(request, context)


@login_required
def add_review(request):
    form = ReviewForm(request.POST, request.FILES)
    if form.is_valid():
        form.instance.name = request.user
        form.save()
    template = 'add_review.html'
    context = {'form': form}
    return render(request, template, context)
