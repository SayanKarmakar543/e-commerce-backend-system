from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from product.models import Product
from product.serializers import ProductSerializer


# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
