from django.contrib import admin

from .models import (
    Airport, Hotel, Ticket, TourPackage, TransportService, Booking, 
    Flight, City, Country
    )
# Register your models here.


@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ['name', ]


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['name', ]


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['user', 'flight', 'ticket_number', 'ticket_class', 'price']


@admin.register(TourPackage)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['image', 'name', 'price', 'duration']


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ['airline', 'flight_number', 'departure_airport', 'arrival_airport', 'price'] 


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', ]


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', ]


@admin.register(TransportService)
class TransportAdmin(admin.ModelAdmin):
    list_display = ['name', 'vehicle_type', 'price_per_day']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'flight', 'tour_package', 'booking_date', 'status']