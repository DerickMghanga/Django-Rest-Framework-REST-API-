from rest_framework import viewsets, mixins

from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    ModelViewset => A viewset that provides default create(), retrieve(), update(), 
    partial_update(), destroy() and list() actions.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' #default

class ProductGenericViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' #default


product_list_view = ProductViewSet.as_view({'get':'list'})
product_detail_view = ProductViewSet.as_view({'get':'retrieve'})