
import json
from pprint import pprint
from django.conf import settings
import requests
# from truecar_garage.garage.get_ads import get_car_ad_details
from pyvin import VIN

from .models import Car
# from truecar_garage.garage.models import Car
# debug_flag = settings.DEBUG
debug_flag = True

def get_data_from_nhtsa(vin_number):
    # National Highway Traffic Safety Administration: NHTSA
    url = 'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesBatch/'
    post_fields = {'format': 'json', 'data':vin_number}
    vin_data_response = requests.post(url, data=post_fields)
    x = json.dumps(vin_data_response.json(), indent=1)
    if debug_flag:
        print(len(vin_data_response.json()['Results'][0]))
    filtered_response = {item: vin_data_response.json()['Results'][0][item] for item in vin_data_response.json()['Results'][0] if vin_data_response.json()['Results'][0][item] != ''}
    if debug_flag:
        pprint(filtered_response)
        print(len(filtered_response)) 
    return filtered_response
    

def generate_or_return_car(vin):
    vehicle_data = get_data_from_nhtsa(vin)
    car_brand = vehicle_data['Make']
    # doors = vehicle_data['Doors']
    try:
        doors = vehicle_data['Doors']
    except:
        doors = 4
    engine_hp = vehicle_data['EngineHP']
    fuel_type = vehicle_data['FuelTypePrimary']
    model = vehicle_data['Model']
    model_year = vehicle_data['ModelYear']
    # series = vehicle_data['Series']
    try:
        series = vehicle_data['Series']
    except:
        series = vehicle_data['Trim']        
    # transmission_speeds = vehicle_data['TransmissionSpeeds']
    try:
        transmission_speeds = vehicle_data['TransmissionSpeeds']
    except:
        transmission_speeds = 6
    # transmission_style = vehicle_data['TransmissionStyle']
    try:
        transmission_style = vehicle_data['transmission_style']
    except:
        transmission_style = 'Automatic'
    if debug_flag:
        print(car_brand)
    if Car.objects.filter(car_brand=car_brand, model=model, model_year=model_year):
        print("Car Already Exist")
        car = Car.objects.filter(car_brand=car_brand, model=model, model_year=model_year)[0]
    else:
        print("Car doesnt exist, Creating ...")
        car = Car(car_brand=car_brand, doors=doors, engine_hp=engine_hp, fuel_type=fuel_type, model=model, model_year=model_year, series=series, transmission_speeds=transmission_speeds, transmission_style=transmission_style)
    # if debug_flag:
    #     print(car)
    #     print(car.car_brand)
    #     print(car.model)
    return car
# cars = get_car_ad_details("bmw", "x4")
# for car in cars:
#     print(car[0])

