from django.db import models
from django.conf import settings  # Import to reference CustomUser

# Create your models here.
class VendorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=255)
    business_address = models.TextField()

    def __str__(self):
        return f"Vendor Profile for {self.user.username}"
