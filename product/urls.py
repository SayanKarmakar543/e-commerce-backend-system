from rest_framework.routers import DefaultRouter
from product.views import ProductViewSet

from django.urls import path, include

router = DefaultRouter()
router.register(r"products", ProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
