import logging
import re
import time

import requests
import bs4
import mysql.connector

TESTING_MODE = True
TRUECAR_BASE_URL = "https://www.truecar.com/"
TRUECAR_TESLA_X_URL = "https://www.truecar.com/used-cars-for-sale/listings/tesla/model-x/"
TRUECAR_BMW_X3_URL = "https://www.truecar.com/used-cars-for-sale/listings/bmw/x3/"
TRUECAR_REGEX = r'.+linkable.+?href="(.+?)">.+<span data-test="vehicleListingPriceAmount">(.+?)</span>.+?</svg>(.+?)<!'

# we assume DB Name is truecar and table name is car
# table has these columns: brand, model, link, price, mileage
DB_NAME = 'truecar'
TABLE_NAME = 'car'

INSERT_STATEMENT = f"INSERT INTO {TABLE_NAME} values ("
SELECT_STATEMENT = f"SELECT * FROM {TABLE_NAME}"
CREATE_TABLE_STATEMENT = f"CREATE TABLE {TABLE_NAME} (brand VARCHAR(50), model VARCHAR(50), link VARCHAR(200), price INT, mileage INT)"

config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "hehe",
    "database": DB_NAME,
}


def get_ad_info(soup: bs4):
    ad_cards_div = soup.findAll('div', {"class": "card-content order-3 vehicle-card-body"})
    ad_list = []
    if TESTING_MODE:
        print(len(ad_cards_div))
    if not len(ad_cards_div):
        print("Response is 200 and No Ad found. Something is not working from Server Side")
    else:
        iterator = 0
        for ad_card_div in ad_cards_div:
            if TESTING_MODE:
                print(ad_card_div)
            ad_groups = re.finditer(TRUECAR_REGEX, str(ad_card_div))
            if ad_groups:
                for ad_group in ad_groups:
                    if TESTING_MODE:
                        print(f"iterator = {iterator}")
                        print("print(ad_price)")
                        print(ad_group)
                        print("print(ad_price.string)")
                        print(ad_group.string)
                    for ad_item in ad_group.groups():
                        if TESTING_MODE:
                            print("ad_item")
                            print(ad_item)
                    ad_list.append([TRUECAR_BASE_URL+ad_group.groups()[0], ad_group.groups()[1][1:], ad_group.groups()[2]])
                if len(ad_list) > 19:
                    break
        if TESTING_MODE:
            print(len(ad_list))
            print(ad_list)
    return ad_list


print("Enter Car Brand")
car_brand = input()

print("Enter Car Model")
car_model = input()
car_model = ''.join(car_model.split())
truecar_url = f"{TRUECAR_BASE_URL}/used-cars-for-sale/listings/{car_brand}/{car_model}/"
if TESTING_MODE:
    print(truecar_url)
truecar_response = requests.request("GET", truecar_url)
if truecar_response.ok:
    if TESTING_MODE:
        print("Response is 200: :))")
    truecar_soup = bs4.BeautifulSoup(truecar_response.text, 'html.parser')
    ad_list = get_ad_info(truecar_soup)
else:
    print("Truecar is not responding correctly!")
    print(truecar_response.status_code)
print("print(ad_list[0])")
# print(ad_list[0])
for ad in ad_list:
    print("hehe\n")
    # print(ad)
    # for ad_item in ad:
    #     print(ad_item)
    print(ad[0])
    print(ad[1])

