from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from django.urls import path, include
from .views import signup_view, login_view, logout_view

# Router
router = DefaultRouter()

# Routes
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]