from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import CategoriesForm
from webapp.models import Products, Categories


def categories_view(request: WSGIRequest):
    categories = Categories.objects.exclude(is_deleted=True)
    context = {
        'categories': categories
    }
    return render(request, 'categories_view.html', context=context)


def delete_category(request, pk):
    category = get_object_or_404(Products, pk=pk)
    return render(request, 'category_confirm_delete.html', context={'category': category})


def confirm_delete_category(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    category.delete()
    return redirect('categories')


def edit_category(request, pk):
    category = get_object_or_404(Categories, pk=pk)

    if request.method == "POST":
        form = CategoriesForm(request.POST, instance=category)
        if form.is_valid():
            category.save()
            return redirect('categories')

    form = CategoriesForm(instance=category)
    return render(request, 'category_edit_view.html', context={'form': form,'category': category})