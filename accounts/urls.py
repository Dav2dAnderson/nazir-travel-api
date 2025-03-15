from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import UserRegistrationViewSet, UserLoginViewSet, UserLogOutViewSet

router = DefaultRouter()

router.register('registration', UserRegistrationViewSet, basename='sign-user-up')
router.register('login', UserLoginViewSet, basename='log-user-in')
router.register('logout', UserLogOutViewSet, basename='log-user-out')

urlpatterns = [
    path('', include(router.urls))
]