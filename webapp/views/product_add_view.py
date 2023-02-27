from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from webapp.forms import ProductsForm
from webapp.models import Products


def product_add_view(request: WSGIRequest):
    if request.method == "GET":
        form = ProductsForm()
        return render(request, "product_add.html", context={"form": form})

    form = ProductsForm(data=request.POST)
    if not form.is_valid():
        return render(request, "product_add.html", context={"form": form})
    else:
        product = Products.objects.create(**form.cleaned_data)
        return redirect("product_view", pk=product.pk)
