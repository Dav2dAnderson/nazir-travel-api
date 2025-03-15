from django.db import models
from django.contrib.auth.models import AbstractUser

from .validators import phone_validator
# Create your models here.


class CustomRole(models.Model):
    CUSTOMER = "customer"
    BRANCH_ADMIN = "branch_admin"
    SITE_ADMIN = 'admin'

    ROLES = (
        (CUSTOMER, 'Mijoz'),
        (BRANCH_ADMIN, 'Filial admin'),
        (SITE_ADMIN, 'Sayt admin')
    )

    name = models.CharField(max_length=100, choices=ROLES)

    def __str__(self):
        return self.name
    

class CustomUser(AbstractUser):
    phone_number = models.CharField(
        max_length=13, validators=[phone_validator], null=True, blank=True, verbose_name="Telefon raqam"
        )
    role = models.ForeignKey(CustomRole, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        if self.role and self.role.name == 'admin':
            self.is_staff = True
        super().save(*args, **kwargs)
    
    
    