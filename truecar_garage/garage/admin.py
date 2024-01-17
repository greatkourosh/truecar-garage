from django.contrib import admin

# Register your models here.
from .models import CarAd, Car

admin.site.register(CarAd)
admin.site.register(Car)
