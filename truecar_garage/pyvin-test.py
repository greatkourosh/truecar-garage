from pyvin import VIN
# from vin_decoder.decode import parse_vin
# https://vpic.nhtsa.dot.gov/
# vehicle = VIN('JT2AE09W4P0038539')
vehicle = VIN('5UX33DT07N9M86282')

print(vehicle.Make, vehicle.Model, vehicle.ModelYear)
# print(vehicle)
# vehicle.Country, vehicle.Type,
print(vehicle.Manufacturer)
print(vehicle.EngineHP)
print(vehicle.EngineModel)
print(vehicle.EngineCylinders)
print(vehicle.FuelTypePrimary)
print(vehicle.PlantCountry)
print(vehicle.Series)
print(vehicle.TransmissionSpeeds)
print(vehicle.TransmissionStyle)



my_vins = ('JT2AE09W4P0038539', 'KMHD35LH5EU205042', '5UX33DT07N9M86282')

my_vehicles = VIN(*my_vins)

# for veh in my_vehicles:
#     print(veh.Make, veh.Model, veh.ModelYear)

# import vin_decoder

# print(parse_vin('5UX33DT07N9M86282'))

# import requests,json
# url = 'https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeId/440?format=json'
# r = requests.get(url)
# print(r.text)