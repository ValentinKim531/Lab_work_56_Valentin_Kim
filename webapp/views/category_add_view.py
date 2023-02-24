from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from webapp.forms import CategoriesForm
from webapp.models import Categories


def category_add_view(request: WSGIRequest):
    if request.method == "GET":
        form = CategoriesForm()
        return render(request, 'category_add.html',
                      context={
                          'form': form
                      })

    form = CategoriesForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'category_add.html',
                      context={
                          'form': form
                      })
    else:
        Categories.objects.create(**form.cleaned_data)
        return redirect('categories')