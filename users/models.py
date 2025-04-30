from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    # Override the groups and user_permissions fields to avoid reverse accessor conflict
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Custom related_name
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions',  # Custom related_name
        blank=True,
    )

    def __str__(self):
        return self.username

    


# class Customization(models.Model):
#     field_name_1 = models.CharField(max_length=100)
#     field_name_2 = models.TextField()


