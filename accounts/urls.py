from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import UserRegistrationViewSet, UserLoginViewSet, UserLogOutView
router = DefaultRouter()

router.register('registration', UserRegistrationViewSet, basename='sign-user-up')
router.register('login', UserLoginViewSet, basename='log-user-in')

urlpatterns = [
    path('', include(router.urls)),
    path('logout/', UserLogOutView.as_view(), name='logout'),
]