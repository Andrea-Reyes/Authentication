from django.db import models

# Create your models here.
class User(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    def __str__(self):
        return self.email