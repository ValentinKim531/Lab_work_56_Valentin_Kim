from django.db import models
from django.utils import timezone


# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Категория")

    def __str__(self):
        return self.name

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Products(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, help_text='Наименование', verbose_name="Наименование")
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Описание")
    category = models.ForeignKey(to='webapp.Categories', verbose_name='Category', null=True, blank=False, related_name='products', on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время обновления")
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.TextField(max_length=500, null=True, blank=True, help_text='Ссылка на изображение', verbose_name="Ссылка на изображение")
    is_deleted = models.BooleanField(verbose_name='удалено', null=False, default=False)

    def __str__(self):
        return f"{self.title} - {self.description} - {self.category} - {self.price} - {self.image} "

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"