from django.urls import path
from webapp.views.products_view import products_view
from webapp.views.product_view import (
    product_view,
    delete_product,
    edit_product,
    confirm_delete,
)

from webapp.views.product_add_view import product_add_view

urlpatterns = [
    path("", products_view, name="products"),
    path("products", products_view, name="products"),
    path("products/add", product_add_view, name="product_add"),
    path("product/<int:pk>", product_view, name="product_view"),
    path("product/delete/<int:pk>", delete_product, name="product_delete"),
    path(
        "product/<int:pk>/confirm_delete/",
        confirm_delete,
        name="confirm_delete",
    ),
    path("products/<int:pk>/edit", edit_product, name="product_edit"),
]
