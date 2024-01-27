from django import urls
from django.conf import settings
from django.urls import include, path

from . import views

app_name = "garage"
urlpatterns = [
    # ex: /garage/
    path("", views.index, name="index"),
    # ex: /garage/car_ad/
    path("car_ad/", views.car_ads_detail, name="car_ads_detail"),
    # ex: /garage/car_ad/2/
    path("car_ad/<int:car_ad_id>/", views.car_ad_detail, name="car_ad_detail"),
    # # ex: /garage/2/
    # path("<int:car_ad_id>/", views.car_ad_detail, name="car_ad_detail"),
    # ex: /garage/car/
    path("car/", views.cars_detail, name="cars_detail"),
    # Display a Car Details @ ex: /garage/car/2/
    # Now add Related Car Ads
    path("car/<int:car_id>/", views.car_detail, name="car_detail"),
    # Now add Related Car Ads
    path("load_car/", views.load_car_view, name="load_car"),
    path("car_generator/", views.car_generator, name="car_generator"),
    path("create_car/", views.create_car, name="create_car"),
    path("select_car/", views.select_car, name="select_car"),
    path("test_form_view/", views.TestFormView.as_view(), name="test_form_default"),
]