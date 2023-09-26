from django.db import models

from users.models import OnsiUser


class Order(models.Model):
    user_id = models.ForeignKey(OnsiUser, on_delete=models.CASCADE, related_name='order')
    address = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    date = models.DateField()
    time = models.TimeField()
    delivery = models.BooleanField(default=False)
    sum = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Product(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=200)
    full_description = models.TextField()
    price = models.PositiveIntegerField()
    status = models.BooleanField(default=False)
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='product')
    image = models.ImageField()

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Value(models.Model):
    name = models.CharField(max_length=100)
    attribute_id = models.ForeignKey('Attribute', on_delete=models.CASCADE, related_name='value')

    class Meta:
        verbose_name = 'Значение'
        verbose_name_plural = 'Значения'


class Attribute(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Атрибут'
        verbose_name_plural = 'Атрибуты'


class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


