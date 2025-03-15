from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import permissions, viewsets, response

from .models import (
    Airport, Hotel, Ticket, TourPackage, TransportService, Booking, 
    Flight, City, Country
    )

from .serializers import (
    AirportSerializer, HotelSerializer, TicketSerializer, TourPackageSerializer, 
    BookingSerializer, TransportServiceSerializer, FlightSerializer
    )

from .permissions import IsAdminOrReadOnly
# Create your views here.


class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]



class AirportViewSet(BaseViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer

    search_fields = ['name', 'city__name', 'country__name']
    ordering_fields = ['name']


class HotelViewSet(BaseViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    search_fields = ['name', 'stars', 'country__name']


class TicketViewSet(BaseViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    search_fields = ['user__username', 'flight__flight_number', 'price', 'ticket_class']
    ordering_fields = ['ticket_number']


class TourPackageViewSet(BaseViewSet):
    queryset = TourPackage.objects.all()
    serializer_class = TourPackageSerializer

    search_fields = ['name', 'duration']


class TransportServiceViewSet(BaseViewSet):
    queryset = TransportService.objects.all()
    serializer_class = TransportServiceSerializer

    search_fields = ['name', 'vehicle_type']


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    search_fields = ['user__username', 'flight__flight_number', 'hotel__name']

    def get_queryset(self):
        user = self.request.user
        if user.role.name in ['branch_admin', 'admin']:
            return Booking.objects.all()
        return Booking.objects.filter(user=user)


class FlightViewSet(BaseViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    search_fields = ['airline', 'flight_number', 'departure_airport__name', 'arrival_airport__name', 'price', 'arrival_time']
