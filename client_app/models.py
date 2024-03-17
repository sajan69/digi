from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, null=True)
    marketing_preferences = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

# Create your models here.
