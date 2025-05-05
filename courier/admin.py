from django.contrib import admin
from .models import CourierProfile

# Registering the CourierProfile model with the Django admin site
# to manage courier profiles through the admin interface.
admin.site.register(CourierProfile)



