from django.urls import path
from user.views import UserRegistrationView

urlpatterns = [
    path(
        "registration/", UserRegistrationView.as_view(), name="user-registration"
    ),
]
