from django import forms
from django.core.exceptions import ValidationError


from webapp.models import Products, Categories


class ProductsForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = ("title", "description", "category", "price", "image")

        labels = {
            "title": 'Заголовок',
            "description": 'Описание',
            "category": 'Категория',
            "price": 'Цена',
            "image": 'Ссылка на изображение'
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise ValidationError("Title must be longer than 2 characters")
        return title

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if len(description) < 2:
            raise ValidationError("Description must be longer than 2 characters")
        return description


class CategoriesForm(forms.ModelForm):

    class Meta:
        model = Categories
        fields = ("name",)

        labels = {"name": 'Название'}

    def clean_title(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise ValidationError("Name must be longer than 2 characters")
        return name

