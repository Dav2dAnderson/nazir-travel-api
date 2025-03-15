from django.contrib import admin

from .models import CustomUser, CustomRole
# Register your models here.


@admin.register(CustomUser)
class CustomUser(admin.ModelAdmin):
    list_display = ['username', 'phone_number']


@admin.register(CustomRole)
class CustomRole(admin.ModelAdmin):
    list_display = ['name', ]


