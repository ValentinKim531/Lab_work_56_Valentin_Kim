from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from webapp.models import Products


def products_view(request: WSGIRequest):
    products = (
        Products.objects.exclude(is_deleted=True)
        .filter(balance__gt=0)
        .order_by("category")
        .order_by("title")
    )
    context = {"products": products}
    return render(request, "products.html", context=context)
