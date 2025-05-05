from django.db import models
from django.conf import settings  # Import to reference CustomUser

class CustomerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    shipping_address = models.TextField()

    def __str__(self):
        return f"Customer Profile for {self.user.username}"
