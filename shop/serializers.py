from rest_framework import serializers as s

from .models import Product, Value, Category, Order, Attribute


class ProductSerializer(s.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ValueSerializer(s.ModelSerializer):
    class Meta:
        model = Value
        fields = '__all__'


class CategorySerializer(s.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class OrderSerializer(s.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class AttributeSerializer(s.ModelSerializer):
    class Meta:
        model = Attribute
        fields = '__all__'
