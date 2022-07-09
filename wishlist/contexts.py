from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def wishlist_contents(request):
    """  Returns shopping wishlist contents"""

    wishlist_items = []
    wishlist_total = 0
    product_count = 0
    wishlist = request.session.get('wishlist', {})

    for item_id, wishlist_quantity in wishlist.items():
        product = get_object_or_404(Product, pk=item_id)
        wishlist_total += wishlist_quantity * product.price
        product_count += wishlist_quantity
        wishlist_items.append({
            'item_id': item_id,
            'wishlist_quantity': wishlist_quantity,
            'product': product,
        })

    if wishlist_total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = wishlist_total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - wishlist_total
    else:
        delivery = 0
        free_delivery_delta = 0

    wishlist_grand_total = delivery + wishlist_total

    context = {
        'wishlist_items': wishlist_items,
        'wishlist_total': wishlist_total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'wishlist_grand_total': wishlist_grand_total,
    }

    return context