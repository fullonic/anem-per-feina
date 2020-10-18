from rest_framework_simplejwt.views import TokenRefreshView  # type: ignore

from django.urls import path

from .custom_claims import MyTokenObtainPairView
from .views import registration

urlpatterns = [
    # path('login/', TokenObtainPairView.as_view()),
    path("register/", registration, name="register"),
    path("login/", MyTokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
]
