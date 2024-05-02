import requests
from bs4 import BeautifulSoup
import csv


# URL of the website containing the table
url = 'https://batchgeo.com/map/cities-latitude-longitude'
add_on = ".html"


cities = []

with open("uscities.csv", "r", newline="", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)

    for row in csvreader:
        city = row[0]
        latitude = row[6]
        longitude = row[7]
        pop = int(row[8])

        cities.append([city, latitude, longitude, pop])

largest_cities = sorted(cities, key=lambda x:x[3])[-100:]

with open('top_100_cities_usa.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["City", "Latitude", "Longitude", "Population"])
    for row in largest_cities:
        writer.writerow(row)    