from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from .models import Product, Category, Value, Attribute, Order
from .serializers import ProductSerializer, CategorySerializer, ValueSerializer, AttributeSerializer, OrderSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, ]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, ]


class ValueViewSet(viewsets.ModelViewSet):
    queryset = Value.objects.all()
    serializer_class = ValueSerializer
    permission_classes = [IsAuthenticated, ]


class AttributeListAPIView(generics.ListAPIView):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, ]
