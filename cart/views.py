from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from cart.serializers import CartItemSerializer, CartSerializer
from cart.models import Cart, CartItem

# Create your views here.
class CartViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
