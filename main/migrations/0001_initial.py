# Generated by Django 5.1.7 on 2025-03-13 16:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=150, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TourPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='tourpackage_images/')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duration', models.IntegerField(help_text='Duration in text')),
            ],
        ),
        migrations.CreateModel(
            name='TransportService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('vehicle_type', models.CharField(choices=[('car', 'Car'), ('bus', 'Bus'), ('van', 'Van')], max_length=50)),
                ('price_per_day', models.DecimalField(decimal_places=2, max_digits=10)),
                ('available_vehicles', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=150, null=True, unique=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.country')),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.country')),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline', models.CharField(max_length=150)),
                ('flight_number', models.CharField(max_length=10, unique=True)),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('available_seats', models.PositiveIntegerField()),
                ('arrival_airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivals', to='main.airport')),
                ('departure_airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departures', to='main.airport')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
                ('stars', models.IntegerField(default=3)),
                ('price_per_night', models.DecimalField(decimal_places=2, max_digits=10)),
                ('available_rooms', models.PositiveIntegerField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.country')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_number', models.CharField(max_length=20, unique=True)),
                ('seat_number', models.CharField(max_length=10)),
                ('issued_date', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.flight')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='pending', max_length=100)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('flight', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.flight')),
                ('hotel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.hotel')),
                ('tickets', models.ManyToManyField(blank=True, to='main.ticket')),
                ('tour_package', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.tourpackage')),
                ('transport_service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.transportservice')),
            ],
        ),
    ]
