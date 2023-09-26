from django.urls import path, include
from rest_framework.routers import DefaultRouter

from shop.views import ProductViewSet, OrderViewSet, CategoryViewSet, ValueViewSet, AttributeViewSet

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')
router.register(r'order', OrderViewSet, basename='order')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'value', ValueViewSet, basename='value')
router.register(r'attribute', AttributeViewSet, basename='attribute')

urlpatterns = [
    path('', include(router.urls)),
]
