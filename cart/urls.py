from rest_framework.routers import DefaultRouter
from cart import views

from django.urls import path, include

router = DefaultRouter()
router.register("carts", views.CartViewSet)
router.register("cart-items", views.CartItemViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
