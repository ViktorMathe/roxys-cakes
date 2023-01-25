from django.shortcuts import render, redirect


def bag(request):
    return render(request, 'bag.html')


def bag_content(request, cake_id):
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if cake_id in list(bag.keys()):
        bag[cake_id] += quantity
    else:
        bag[cake_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
