from django.urls import path

from webapp.views.categories_view import delete_category, categories_view, edit_category, confirm_delete_category
from webapp.views.category_add_view import category_add_view
from webapp.views.products_view import products_view
from webapp.views.product_view import product_view, delete_product, edit_product, confirm_delete

from webapp.views.product_add_view import product_add_view

urlpatterns = [
    path("", products_view, name='products'),
    path('products', products_view, name='products'),
    path('categories', categories_view, name='categories'),
    path('products/add', product_add_view, name='product_add'),
    path('categories/add', category_add_view, name='category_add'),
    path('product/<int:pk>', product_view, name='product_view'),
    path('product/delete/<int:pk>', delete_product, name='product_delete'),
    path('product/<int:pk>/confirm_delete/', confirm_delete, name='confirm_delete'),
    path('category/delete/<int:pk>', delete_category, name='category_delete'),
    path('category/<int:pk>/confirm_delete_category/', confirm_delete_category, name='confirm_delete_category'),
    path('categories/<int:pk>/edit', edit_category, name='category_edit'),
    path('products/<int:pk>/edit', edit_product, name='product_edit')
]

