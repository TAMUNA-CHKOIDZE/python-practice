from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from products.filters import ProductFilter
from products.models import Product
from products.pagination import ProductsPagination
from products.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductsPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
