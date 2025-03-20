from rest_framework import serializers

from .models import (
    Airport, Hotel, Ticket, TourPackage, TransportService, Booking, 
    Flight, City, Country
    )


class AirportSerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(source='city.name', read_only=True)
    country_name = serializers.CharField(source='country.name', read_only=True)
    class Meta:
        model = Airport
        fields = ['id', 'name', 'city', 'city_name', 'country', 'country_name']


class HotelSerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(source='city.name', read_only=True)
    country_name = serializers.CharField(source='country.name', read_only=True)
    class Meta:
        model = Hotel
        fields = ['id', 'name', 'city', 'city_name', 'country', 'country_name', 'stars', 'price_per_night', 'available_rooms']


class TicketSerializer(serializers.ModelSerializer):
    flight_number = serializers.CharField(source='flight.flight_number', read_only=True)
    user_name = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Ticket
        fields = ['id', 'user', 'user_name', 'flight', 'flight_number', 'ticket_number', 'seat_number', 'ticket_class', 'issued_date', 'price']


class TourPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourPackage
        fields = ['id', 'image', 'name', 'description', 'price', 'discount_price', 'duration']


class TransportServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportService
        fields = ['id', 'name', 'vehicle_type', 'price_per_day', 'available_vehicles']


class BookingSerializer(serializers.ModelSerializer):
    flight_number = serializers.CharField(source='flight.flight_number', read_only=True)
    user_name = serializers.CharField(source='user.username', read_only=True)
    hotel_name = serializers.CharField(source='hotel.name', read_only=True)
    tour_package_name = serializers.CharField(source='tour_package.name', read_only=True)
    transport_service_name = serializers.CharField(source='transport_service.name', read_only=True)
    ticket_number = serializers.CharField(source='tickets.ticket_number', read_only=True)
    class Meta:
        model = Booking
        fields = [
            'id', 'user', 'user_name', 
            'flight', 'flight_number', 
            'hotel', 'hotel_name', 
            'tour_package', 'tour_package_name',
            'transport_service', 'transport_service_name',
            'tickets', 'ticket_number', 
            'booking_date', 'status'
            ]


class FlightSerializer(serializers.ModelSerializer):
    departure_airport_name = serializers.CharField(source='departure_airport.name', read_only=True)
    arrival_airport_name = serializers.CharField(source='arrival_airport.name', read_only=True)
    class Meta:
        model = Flight
        fields = [
            'id', 'airline', 'flight_number', 
            'departure_airport', 'departure_airport_name',
            'arrival_airport', 'arrival_airport_name',
            'departure_time', 'arrival_time', 'price', 'available_seats'
            ]


class CitySerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(source='country.name', read_only=True)
    class Meta:
        model = City
        fields = ['id', 'name', 'country', 'country_name']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', ]
