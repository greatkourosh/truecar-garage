import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# Create your models here.
# class Color(models.Model):
#     color_name = models.CharField(max_length=100)


class Car(models.Model):
    # car_brand = models.CharField(max_length=100)
    class Brand(models.TextChoices):
        TOYOTA = "TYT", "Toyota"
        FORD = "FRD", "Ford"
        CHEVROLET = "CHV", "Chevrolet"
        HONDA = "HND", "Honda"
        NISSAN = "NSN", "Nissan"
        JEEP = "JEP", "Jeep"
        HYUNDAI = "HYN", "Hyundai"
        KIA = "KIA", "Kia"
        RAM = "RAM", "Ram Trucks"
        SUBARU = "SBR", "Subaru"
        GMC = "GMC", "GMC"
        VOLKSWAGEN = "VSW", "Volkswagen"
        BMW = "BMW", "BMW"
        Mazda = "MZD", "Mazda"
        MERCEDES = "BNZ", "Mercedes Benz"
        LEXUS = "LXS", "Lexus"
        TESLA = "TSL", "Tesla"
        DODGE = "DDG", "Dodge"
        AUDI = "AUD", "Audi"
        BUICK = "BUK", "Buick"
        ACURA = "ACR", "Acura"
        VOLVO = "VLV", "Volvo"
        CADILLAC = "CDL", "Cadillac"
        CHRYSLER = "CRY", "Chrysler"
        MITSUBISHI = "MSH", "Mitsubishi"
        LANDROVER = "LND", "Land Rover"
        LINCOLN = "LCN", "Lincoln"
        PORSCHE = "PCH", "Porsche"
        INFINITI = "INF", "Infiniti"
        GENESIS = "GNS", "Genesis"
        MINI = "MIN", "Mini"
        MASERATI = "MSR", "Maserati"
        ALFAROMEO = "AFR", "Alfa Romeo"
        JAGUAR = "JGR", "Jaguar"
        BENTLEY = "BNT", "Bentley"
        FERRARI = "FRR", "Ferrari"
        LAMBORGHINI = "LMB", "Lamborghini"
        ASTINMARTIN = "ASM", "Aston Martin"

    car_brand = models.CharField(
        max_length=3,
        choices=Brand,
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
        choices=Fuel,
        default=Fuel.PETROL,
    )

    listed = models.DateTimeField(
        verbose_name=_("Listed On"),
        default=datetime.date.today,
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
        choices=TransmissionTypes,
        default=TransmissionTypes.MANUAL,
    )

    def __str__(self):
        # return f"{self.car_brand} - {self.model}"
        return f"{self.get_car_brand_display()} - {self.model}"


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
        WHITE: "white",
        BLACK: "black",
        GRAY: "gray",
        SILVER: "silver",
        BLUE: "blue",
        RED: "red",
        BROWN: "brown",
        GREEN: "green",
        ORANGE: "orange",
        BEIGE: "beige",
        PURPLE: "purple",
        GOLD: "gold",
        YELLOW: "yellow",
    }
    exterior_color = models.CharField(
        max_length=3,
        choices=COLOR,
        default=WHITE,
    )
    mileage = models.IntegerField(
        default=0,
    )
    vin = models.CharField(
        max_length=17,
    )
    listed = models.DateTimeField(
        verbose_name=_("Listed On"),
        # default=datetime.datetime.now(),
        auto_now_add=True
    )
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        # return f"{self.car.car_brand} {self.car.model} was published at {self.listed} with VIN = {self.vin}"
        return f"{self.car.get_car_brand_display()} {self.car.model} was published at {self.listed} with VIN = {self.vin}"

    def was_published_recently(self):
        return self.listed >= timezone.now() - datetime.timedelta(days=1)
