import requests
from pyvin import VIN

# https://vpic.nhtsa.dot.gov/
# National Highway Traffic Safety Administration: NHTSA
NHTSA_API_URL = 'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesBatch/'
post_fields = {'format': 'json', 'data': '5UX33DT07N9M86282'}


def vin_decoder(vin):
    vin_request = requests.post(NHTSA_API_URL, data=post_fields)
    not_null_values = {item: vin_request.json()['Results'][0][item] for item in vin_request.json()['Results'][0]
                       if vin_request.json()['Results'][0][item] != ''}
    print(type(not_null_values))
    vehicle_data = []
    vehicle = VIN(vin)
    return vehicle


my_vehicle = vin_decoder('5UX33DT07N9M86282')
# print(my_vehicle)
