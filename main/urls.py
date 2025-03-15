from django.urls import path, include

from .views import AirportViewSet, HotelViewSet, TourPackageViewSet, BookingViewSet, TransportServiceViewSet, FlightViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('airport', AirportViewSet, basename='airport')
router.register('hotel', HotelViewSet, basename='hotel')
router.register('tour-package', TourPackageViewSet, basename='tour-package')
router.register('booking', BookingViewSet, basename='booking')
router.register('transport-service', TransportServiceViewSet, basename='transport-service')
router.register('flight', FlightViewSet, basename='flight')

urlpatterns = [
    path('', include(router.urls))
]


