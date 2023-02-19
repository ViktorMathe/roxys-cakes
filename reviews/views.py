from django.shortcuts import render, get_object_or_404, redirect, reverse
from .forms import ReviewForm
from .models import Reviews
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def reviews(request):
    reviews = Reviews.objects.filter(status=1)
    template = 'reviews.html'
    context = {'reviews': reviews}
    return render(request, template, context)


@login_required
def add_review(request):
    form = ReviewForm(request.POST, request.FILES)
    if form.is_valid():
        form.instance.name = request.user
        form.save()
        messages.success(request, 'Your review has been added!')
    template = 'add_review.html'
    context = {'form': form}
    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Reviews, id=review_id)
    review.delete()
    messages.warning(request, 'Your review has been deleted!')
    return redirect(reverse('reviews'))


@login_required()
def edit_review(request, review_id):
    review = get_object_or_404(Reviews, id=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.warning(request, 'Your review has been edited!')
            return redirect(reverse('reviews'))
    else:
        form = ReviewForm(instance=review)

    template = 'edit_review.html'
    context = {'form': form,
               'review': review}
    return render(request, template, context)
