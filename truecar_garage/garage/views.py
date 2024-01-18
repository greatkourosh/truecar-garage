from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# from truecar_garage.garage.models import CarAd
from .models import CarAd, Car
debug_flag = settings.DEBUG


def index(request):
    # # return HttpResponse("Hello, world. You're at the garage index.")
    # latest_car_ad_list = CarAd.objects.order_by("-listed")[:5]
    # output = ", ".join([str(car_ad) for car_ad in latest_car_ad_list])
    # [print(car_ad) for car_ad in latest_car_ad_list]
    # return HttpResponse(output)
    return car_ads_detail(request, html_template="index")


def cars_detail(request, html_template="cars_detail"):
    # return HttpResponse("You're looking at Car %s." % car_id)
    latest_car_list = Car.objects.order_by("-listed")[:5]
    # output = ", ".join([str(car_ad) for car_ad in latest_car_list])
    # [print(car) for car in latest_car_list]
    # return HttpResponse(output)
    template = loader.get_template(f"garage/{html_template}.html")
    context = {
        "latest_car_list": latest_car_list,
        "page_name": html_template,
        'debug_flag': debug_flag,
    }
    return HttpResponse(template.render(context, request))


def car_detail(request, car_id, html_template="car_detail"):
    # return HttpResponse("You're looking at Car %s." % car_id)
    # latest_car_list = Car.objects.get(id=car_id)
    # output = ", ".join([str(car_ad) for car_ad in latest_car_list])
    # [print(car) for car in latest_car_list]
    # return HttpResponse(latest_car_list)
    car_detail = Car.objects.get(id=car_id)
    template = loader.get_template(f"garage/car_detail.html")
    context = {
        "car_detail": car_detail,
        "page_name": html_template,
        'debug_flag': debug_flag,
    }
    return HttpResponse(template.render(context, request))


def car_ads_detail(request, html_template="car_ads_detail"):
    # return HttpResponse("You're looking at CarAd %s." % car_ad_id)
    latest_car_ad_list = CarAd.objects.order_by("-listed")[:5]
    # output = ", ".join([str(car_ad) for car_ad in latest_car_ad_list])
    # [print(car_ad) for car_ad in latest_car_ad_list]
    # return HttpResponse(output)
    template = loader.get_template(f"garage/{html_template}.html")
    context = {
        "latest_car_ad_list": latest_car_ad_list,
        "page_name": html_template,
        'debug_flag': debug_flag,
    }
    return HttpResponse(template.render(context, request))


def car_ad_detail(request, car_ad_id, html_template="car_ad_detail"):
    # return HttpResponse("You're looking at CarAd %s." % car_ad_id)
    # latest_car_ad_list = CarAd.objects.get(id=car_ad_id)
    # output = ", ".join([str(car_ad) for car_ad in latest_car_ad_list])
    # [print(car_ad) for car_ad in latest_car_ad_list]
    # return HttpResponse(latest_car_ad_list)
    car_ad_detail = CarAd.objects.get(id=car_ad_id)
    template = loader.get_template(f"garage/car_ad_detail.html")
    context = {
        "car_ad_detail": car_ad_detail,
        "page_name": html_template,
        'debug_flag': debug_flag,
    }
    return HttpResponse(template.render(context, request))
