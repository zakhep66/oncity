from django.urls import path, include
from rest_framework.routers import DefaultRouter

from shop.views import ProductViewSet, OrderViewSet, CategoryViewSet, ValueViewSet, AttributeListAPIView

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')
router.register(r'order', OrderViewSet, basename='order')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'value', ValueViewSet, basename='value')

urlpatterns = [
    path('', include(router.urls)),
    path('filter-attributes', AttributeListAPIView.as_view()),
]
