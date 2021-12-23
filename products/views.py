from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from .filters import ProductFilter
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_class = ProductFilter
    search_fields = ['name', 'price']
    ordering_fields = ['name', 'price']


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
