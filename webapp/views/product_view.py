from django.shortcuts import render, get_object_or_404, redirect
from django.core.handlers.wsgi import WSGIRequest

from webapp.forms import ProductsForm
from webapp.models import Products


def product_view(request, pk):
    product = get_object_or_404(Products, pk=pk)
    return render(request, 'product_view.html', context={
        'product': product
    })


def delete_product(request, pk):
    product = get_object_or_404(Products, pk=pk)
    return render(request, 'product_confirm_delete.html', context={'product': product})


def confirm_delete(request, pk):
    product = get_object_or_404(Products, pk=pk)
    product.delete()
    return redirect('products')


def edit_product(request, pk):
    product = get_object_or_404(Products, pk=pk)

    if request.method == "POST":
        form = ProductsForm(request.POST, instance=product)
        if form.is_valid():
            product.save()
            return redirect('product_view', pk=product.pk)

    form = ProductsForm(instance=product)
    return render(request, 'product_edit_view.html', context={'form': form,'product': product})