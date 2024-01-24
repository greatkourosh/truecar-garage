from django.contrib import admin

# Register your models here.
from .models import CarAd, Car

class CarAdmin(admin.ModelAdmin):
    fields = ["car_brand", "model", "series", "model_year", "engine_hp", "fuel_type", "transmission_style"]
    list_display = ["car_brand", "model", "model_year"]
    list_filter = ["car_brand", "model", "model_year"]
    
class CarAdAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["exterior_color", "mileage", "price"]}),
        ("Related Car Detail", {"fields": ["car"]}),
    ]
    # fields = ["car", "exterior_color", "mileage", "price"]
    # readonly_fields=["exterior_color"]
    list_display = ["car", "mileage", "price"]
    list_filter = ["car", "mileage", "price"]

admin.site.register(CarAd, CarAdAdmin)
admin.site.register(Car, CarAdmin)
