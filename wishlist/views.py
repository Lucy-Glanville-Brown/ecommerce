from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages

from products.models import Product


def view_wishlist(request):
    """ A view that renders the wishlist contents page """

    return render(request, 'wishlist/wishlist.html')


def add_to_wishlist(request, item_id):
    """ Add a quantity of the specified product to the wishlist """

    product = get_object_or_404(Product, pk=item_id)

    wishlist_quantity = int(request.POST.get('wishlist_quantity'))
    redirect_url = request.POST.get('redirect_url')
    wishlist = request.session.get('wishlist', {})

    if item_id in list(wishlist.keys()):
        wishlist[item_id] += wishlist_quantity
        messages.success(request,
                         f'Updated {product.name} quantity to {wishlist[item_id]}')
    else:
        wishlist[item_id] = wishlist_quantity
        messages.success(request, f'Added {product.name} to your wishlist')

    request.session['wishlist'] = wishlist
    return redirect(redirect_url)


def adjust_wishlist(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)

    wishlist_quantity = int(request.POST.get('wishlist_quantity'))
    wishlist = request.session.get('wishlist', {})
    if wishlist_quantity > 0:
        wishlist[item_id] = wishlist_quantity
        messages.success(request,
                         f'Updated {product.name} wishlist_quantity to {wishlist[item_id]}')
    else:
        wishlist.pop(item_id)
        messages.success(request, f'Removed {product.name} from your wishlist')

    request.session['wishlist'] = wishlist
    return redirect(reverse('view_wishlist'))


def remove_from_wishlist(request, item_id):
    """Remove the item from the shopping wishlist"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        wishlist = request.session.get('wishlist', {})
        wishlist.pop(item_id)
        messages.success(request, f'Removed {product.name} from your wishlist')

        request.session['wishlist'] = wishlist
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)