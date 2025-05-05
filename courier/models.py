from django.db import models
from django.conf import settings  # Import to reference CustomUser

class CourierProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=100)
    delivery_area = models.CharField(max_length=255)

    def __str__(self):
        return f"Courier Profile for {self.user.username}"
