from django.db import models
from django.utils.text import slugify

from accounts.models import CustomUser

# Create your models here.


class Airport(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, null=True, blank=True)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Country(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, null=True, blank=True, unique=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
 

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=150, null=True, blank=True, unique=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    

class Flight(models.Model):
    airline = models.CharField(max_length=150)
    flight_number = models.CharField(max_length=10, unique=True)
    departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')
    arrival_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_seats = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.airline} {self.flight_number}"


class Ticket(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    ticket_number = models.CharField(max_length=20, unique=True)
    seat_number = models.CharField(max_length=10)
    ticket_class = models.CharField(max_length=50, choices=[
        ('economy', 'Economy'), ('business', 'Business'), ('first', 'First class')
        ], default='economy'),
    issued_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Ticket {self.ticket_number}"


class TourPackage(models.Model):
    image = models.ImageField(upload_to='tourpackage_images/')
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(help_text='Duration in text')
    
    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, null=True, blank=True, unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    stars = models.IntegerField(default=3)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    available_rooms = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class TransportService(models.Model):
    name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=50, choices=[
        ('car', 'Car'), ('bus', 'Bus'), ('van', 'Van')
    ])
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    available_vehicles = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    flight = models.ForeignKey(Flight, on_delete=models.SET_NULL, null=True, blank=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True, blank=True)
    tour_package = models.ForeignKey(TourPackage, on_delete=models.SET_NULL, null=True, blank=True)
    transport_service = models.ForeignKey(TransportService, on_delete=models.SET_NULL, null=True, blank=True)
    tickets = models.ManyToManyField(Ticket, blank=True)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=[
        ('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')
    ], default='pending')

    def __str__(self):
        return f"Booking {self.id}"
        