from django import template
from ..models import Cart
from django.db.models import Q
register = template.Library()

@register.simple_tag
def total_items(request):
    items = request.user.cart.cartitem_set.filter(
        Q(checked=False) &
        Q(active=True))
    return items.count()