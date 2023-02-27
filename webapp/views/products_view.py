from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from webapp.forms import SearchForm
from webapp.models import Products
from django.contrib.postgres.search import SearchVector


def products_view(request: WSGIRequest):
    products = (
        Products.objects.exclude(is_deleted=True)
        .filter(balance__gt=0)
        .order_by("category")
        .order_by("title")
    )

    form = SearchForm()
    query = None
    results = []
    if "query" in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            results = Products.objects.annotate(
                search=SearchVector("title"),
            ).filter(search=query)

    context = {
        "products": products,
        "form": form,
        "query": query,
        "results": results,
    }
    return render(request, "products.html", context=context)
