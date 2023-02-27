from django.contrib import admin

from webapp.models import Products

# Register your models here.


class Products_Admin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "category",
        "price",
        "image",
        "balance",
    )
    list_filter = (
        "id",
        "title",
        "description",
        "category",
        "price",
        "image",
        "balance",
    )
    search_fields = ("title", "description", "category", "price", "balance")
    fields = ("title", "description", "category", "price", "image", "balance")
    readonly_fields = ("id", "created_at", "updated_at")


admin.site.register(Products, Products_Admin)
