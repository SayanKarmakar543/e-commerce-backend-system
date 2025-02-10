from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from order.serializers import OrderSerializer, OrderItemSerializer
from order.models import Order, OrderItem


# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
