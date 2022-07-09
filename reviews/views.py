from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Review
from .forms import ReviewForm

from products.models import Product
from profiles.models import UserProfile


@login_required
def add_review(request, product_id):
    """ Allows a user to add a review """

    product = get_object_or_404(Product, pk=product_id)
    user = get_object_or_404(UserProfile, user=request.user)

    if request.user.is_authenticated:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = user
            review.save()
            messages.success(request, 'Thank You! Your review \
                has now been posted!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Oops, something went wrong! \
                Please try adding your review again.')

    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'reviews/add_review.html', context)
