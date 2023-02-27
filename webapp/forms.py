from django import forms
from django.core.exceptions import ValidationError


from webapp.models import Products


class GeeksForm(forms.Form):
    geeks_field = forms.IntegerField(min_value=1)


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = (
            "title",
            "description",
            "category",
            "price",
            "image",
            "balance",
        )

        labels = {
            "title": "Заголовок",
            "description": "Описание",
            "category": "Категория",
            "price": "Цена",
            "image": "Ссылка на изображение",
            "balance": "Остаток",
        }

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) < 2:
            raise ValidationError("Title must be longer than 2 characters")
        return title

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if len(description) < 2:
            raise ValidationError(
                "Description must be longer than 2 characters"
            )
        return description
