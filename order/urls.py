from rest_framework.routers import DefaultRouter
from order import views

from django.urls import path, include

router = DefaultRouter()
router.register("orders", views.OrderViewSet)
router.register("order-items", views.OrderItemViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
