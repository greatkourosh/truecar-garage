from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse
from django.template import loader

from .car_generator import generate_or_return_car

from .get_ads import get_car_ad_details
from .models import CarAd, Car
# import true_car.true_car.get_ads
debug_flag = settings.DEBUG

TRUE_CAR_AD_URL = "https://www.truecar.com/used-cars-for-sale/listing/"

def index(request, html_template="car_ads_detail"):
    # # return HttpResponse("Hello, world. You're at the garage index.")
    # latest_car_ad_list = CarAd.objects.order_by("-listed")[:5]
    # output = ", ".join([str(car_ad) for car_ad in latest_car_ad_list])
    # [print(car_ad) for car_ad in latest_car_ad_list]
    # return HttpResponse(output)
    return car_ads_detail(request, html_template)


def cars_detail(request, html_template="cars_detail"):
    # return HttpResponse("You're looking at Car %s." % car_id)
    # latest_car_list = Car.objects.order_by("-listed")[:5]
    # output = ", ".join([str(car_ad) for car_ad in latest_car_list])
    # [print(car) for car in latest_car_list]
    # return HttpResponse(output)
    # template = loader.get_template(f"garage/{html_template}.html")
    # context = {
    #     "latest_car_list": latest_car_list,
    #     "page_name": html_template,
    #     'debug_flag': debug_flag,
    # }
    # return HttpResponse(template.render(context, request))
    try:
        # latest_car_list = Car.objects.order_by("-car_brand")[:5]
        latest_car_list = Car.objects.order_by("-car_brand")
        context = {
            "latest_car_list": latest_car_list,
            "page_name": html_template,
            'debug_flag': debug_flag,
        }
    except Car.DoesNotExist:
        raise Http404("Car does not exist")
    return render(request, f"garage/{html_template}.html", context)


def car_detail(request, car_id, html_template="car_detail"):
    # return HttpResponse("You're looking at Car %s." % car_id)
    # latest_car_list = Car.objects.get(id=car_id)
    # output = ", ".join([str(car_ad) for car_ad in latest_car_list])
    # [print(car) for car in latest_car_list]
    # return HttpResponse(latest_car_list)
    # car_detail = Car.objects.get(id=car_id)
    # related_car_ads = CarAd.objects.get(car=car_id)
    related_car_ads = CarAd.objects.filter(car=car_id)
    # template = loader.get_template(f"garage/car_detail.html")
    car_detail = get_object_or_404(Car, pk=car_id)
    context = {
        "car_detail": car_detail,
        "related_car_ads": related_car_ads,
        "page_name": html_template,
        'debug_flag': debug_flag,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, f"garage/{html_template}.html", context)


def car_ads_detail(request, html_template="car_ads_detail"):
    # return HttpResponse("You're looking at CarAd %s." % car_ad_id)
    latest_car_ad_list = CarAd.objects.order_by("-listed")[:5]
    # output = ", ".join([str(car_ad) for car_ad in latest_car_ad_list])
    # [print(car_ad) for car_ad in latest_car_ad_list]
    # return HttpResponse(output)
    # template = loader.get_template(f"garage/{html_template}.html")
    context = {
        "latest_car_ad_list": latest_car_ad_list,
        "page_name": html_template,
        "debug_flag": debug_flag,
        "truecar_link": TRUE_CAR_AD_URL,
        
    }
    # return HttpResponse(template.render(context, request))
    return render(request, f"garage/{html_template}.html", context)


def car_ad_detail(request, car_ad_id, html_template="car_ad_detail"):
    # return HttpResponse("You're looking at CarAd %s." % car_ad_id)
    # latest_car_ad_list = CarAd.objects.get(id=car_ad_id)
    # output = ", ".join([str(car_ad) for car_ad in latest_car_ad_list])
    # [print(car_ad) for car_ad in latest_car_ad_list]
    # return HttpResponse(latest_car_ad_list)
    car_ad_detail = CarAd.objects.get(id=car_ad_id)
    # template = loader.get_template(f"garage/car_ad_detail.html")
    context = {
        "car_ad_detail": car_ad_detail,
        "page_name": html_template,
        'debug_flag': debug_flag,
        "truecar_link": TRUE_CAR_AD_URL,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, f"garage/{html_template}.html", context)

# This REGEX returns 5 Item:
# 0) Link
# 1) Price
# 2) Mileage
# 3) Color
# 4) VIN
def load_car(request, html_template="load_car"):
    car_ads_data = get_car_ad_details("bmw", "z4")
    for car_ad_data in car_ads_data:
        # print(f"car_ad[4] = {car_ad[4]}")
        # print(f"car_ad = {car_ad}")
        
        car = generate_or_return_car(car_ad_data[4])
        try:
            car.save()
        except:
            pass
        # if debug_flag:
        #     print(car)
        #     print(car.car_brand)
        #     print(car.model)
        if CarAd.objects.filter(vin=car_ad_data[4]):
            CarAd.objects.get(vin=car_ad_data[4]).delete()
        car_ad = CarAd(exterior_color=car_ad_data[3], mileage=int(car_ad_data[2]), vin=car_ad_data[4], price=car_ad_data[1], true_car_link=car_ad_data[0], car=car)
        print(f"exterior_color = {car_ad.exterior_color}")
        car_ad.save()
    context = {
        "cars": car_ads_data,
        "page_name": html_template,
        'debug_flag': debug_flag,
    }
    return render(request, f"garage/{html_template}.html", context)
    
def car_generator(request, html_template="load_car"):
    car = generate_or_return_car('5UXTY5C0XM9H22657')
    context = {
        "car": car,
        "page_name": html_template,
        'debug_flag': debug_flag,
    }
    return HttpResponse("ok")