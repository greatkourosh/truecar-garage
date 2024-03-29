import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
# from djmoney.models.fields import MoneyField
from django.utils.translation import gettext_lazy as _


# Create your models here.
# class Color(models.Model):
#     color_name = models.CharField(max_length=100)


class Car(models.Model):
    # car_brand = models.CharField(max_length=100)
    class Brand(models.TextChoices):
        TOYOTA = "Toyota", "Toyota"
        FORD = "Ford", "Ford"
        CHEVROLET = "Chevrolet", "Chevrolet"
        HONDA = "Honda", "Honda"
        NISSAN = "Nissan", "Nissan"
        JEEP = "Jeep", "Jeep"
        HYUNDAI = "Hyundai", "Hyundai"
        KIA = "Kia", "Kia"
        RAM = "Ram Trucks", "Ram Trucks"
        SUBARU = "Subaru", "Subaru"
        GMC = "GMC", "GMC"
        VOLKSWAGEN = "Volkswagen", "Volkswagen"
        BMW = "BMW", "BMW"
        Mazda = "Mazda", "Mazda"
        MERCEDES = "Mercedes Benz", "Mercedes Benz"
        LEXUS = "Lexus", "Lexus"
        TESLA = "Tesla", "Tesla"
        DODGE = "Dodge", "Dodge"
        AUDI = "Audi", "Audi"
        BUICK = "Buick", "Buick"
        ACURA = "Acura", "Acura"
        VOLVO = "Volvo", "Volvo"
        CADILLAC = "Cadillac", "Cadillac"
        CHRYSLER = "Chrysler", "Chrysler"
        MITSUBISHI = "Mitsubishi", "Mitsubishi"
        LANDROVER = "Land Rover", "Land Rover"
        LINCOLN = "Lincoln", "Lincoln"
        PORSCHE = "Porsche", "Porsche"
        INFINITI = "Infiniti", "Infiniti"
        GENESIS = "Genesis", "Genesis"
        MINI = "Mini", "Mini"
        MASERATI = "Maserati", "Maserati"
        ALFAROMEO = "Alfa Romeo", "Alfa Romeo"
        JAGUAR = "Jaguar", "Jaguar"
        BENTLEY = "Bentley", "Bentley"
        FERRARI = "Ferrari", "Ferrari"
        LAMBORGHINI = "Lamborghini", "Lamborghini"
        ASTINMARTIN = "Aston martin", "Aston martin"

    car_brand = models.CharField(
        max_length=25,
        choices=Brand.choices,
        default=Brand.TOYOTA,
    )

    # def get_car_brand(self):
    #     return self.Brand.label

    doors = models.IntegerField(
        default=4
    )
    engine_hp = models.IntegerField()
    # FUEL = {
    #     "DIESEL": "Diesel",
    #     "PETROL": "Petrol",
    #     "HYBRID": "Hybrid",
    #     "ELECTRIC": "Electric",
    #     "BIOFUELS": "Biofuels",
    #     "HYDROGEN": "Hydrogen",
    #     "GAS": "Natural Gas",
    #     "ETHANOL": "Ethanol",
    # }

    class Fuel(models.TextChoices):
        DIESEL = "DSL", "Diesel"
        PETROL = "PTR", "Petrol"
        HYBRID = "HYB", "Hybrid"
        ELECTRIC = "ELC", "Electric"
        BIOFUELS = "BIO", "Biofuels"
        HYDROGEN = "HDR", "Hydrogen"
        GAS = "GAS", "Natural Gas"
        ETHANOL = "ETH", "Ethanol"
        
    fuel_type = models.CharField(
        max_length=3,
        choices=Fuel.choices,
        default=Fuel.PETROL,
    )
    # car_model = models.CharField(max_length=100)
    model = models.CharField(
        max_length=50,
    )
    model_year = models.IntegerField(
        default=datetime.datetime.now().year,
        validators=[
            MaxValueValidator(2999),
            MinValueValidator(1900)
        ]
    )
    series = models.CharField(
        max_length=50,
    )
    transmission_speeds = models.IntegerField(
        default=6,
        validators=[
            MaxValueValidator(18),
        ]
    )

    class TransmissionTypes(models.TextChoices):
        MANUAL = "MNU", "Manual"
        AUTOMATIC = "ATO", "Automatic"
        TIPTRONIC = "TPT", "Tiptronic"
        SEMIAUTOMATIC = "SMA", "Semi-Automatic"
        DUALCLUTCH = "DCL", "Dual-Clutch"
        CVT = "CVT", "Continuously Variable Transmission"

    # TRANSMISSION_TYPES = {
    #     "MANUAL": "Manual",
    #     "AUTOMATIC": "Automatic",
    #     "TIPTRONIC": "Tiptronic",
    #     "SEMIAUTOMATIC": "Semi-Automatic",
    #     "DUALCLUTCH": "Dual-Clutch",
    #     "CVT": "Continuously Variable Transmission"
    # }
    transmission_style = models.CharField(
        max_length=3,
        choices=TransmissionTypes.choices,
        default=TransmissionTypes.MANUAL,
    )

    def __str__(self):
        # return f"{self.car_brand} - {self.model}"
        return f"{self.get_car_brand_display()} - {self.model} - {self.model_year}"


class CarAd(models.Model):
    # COLOR = {
    #     "WHI": "white",
    #     "BLK": "black",
    #     "GRY": "gray",
    #     "SLV": "silver",
    #     "BLU": "blue",
    #     "RED": "red",
    #     "BRW": "brown",
    #     "GRN": "green",
    #     "ORG": "orange",
    #     "BIG": "beige",
    #     "PRP": "purple",
    #     "GLD": "gold",
    #     "YLW": "yellow",
    # }
    WHITE = "WHI"
    BLACK = "BLK"
    GRAY = "GRY"
    SILVER = "SLV"
    BLUE = "BLU"
    RED = "RED"
    BROWN = "BRW"
    GREEN = "GRN"
    ORANGE = "ORG"
    BEIGE = "BIG"
    PURPLE = "PRP"
    GOLD = "GLD"
    YELLOW = "YLW"
    COLOR = {
        WHITE: "White",
        BLACK: "Black",
        GRAY: "Gray",
        SILVER: "Silver",
        BLUE: "Blue",
        RED: "Red",
        BROWN: "Brown",
        GREEN: "Green",
        ORANGE: "Orange",
        BEIGE: "Beige",
        PURPLE: "Purple",
        GOLD: "Gold",
        YELLOW: "Yellow",
    }
    exterior_color = models.CharField(
        max_length=3,
        # choices=COLOR,
        default="White",
    )
    mileage = models.IntegerField(
        default=0,
    )
    vin = models.CharField(
        max_length=17,
        unique=True,
    )
    listed = models.DateTimeField(
        verbose_name=_("Listed On"),
        default=datetime.datetime.now(),
        # auto_now_add=True,
    )
    price = models.DecimalField(
        max_digits=6,
        default=0,
        decimal_places=0
    )
    
    true_car_link = models.URLField(
        max_length=200,
        blank=True,
        unique=False,
        verbose_name="Ad Link in TrueCar Website",
    )
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        # return f"{self.car.car_brand} {self.car.model} was published at {self.listed} with VIN = {self.vin}"
        return f"{self.car.get_car_brand_display()} {self.car.model} was published at {self.listed} with VIN = {self.vin}"

    def was_published_recently(self):
        return self.listed >= timezone.now() - datetime.timedelta(days=1)
