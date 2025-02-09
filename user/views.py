from user.serializers import UserRegistrationSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

# Create your views here.
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
