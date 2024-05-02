import requests
from bs4 import BeautifulSoup
import csv

largest_cities = {}

largest_url = "http://www.citymayors.com/gratis/uk_topcities.html"
response = requests.get(largest_url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table containing the city data
    table = soup.find('table')

    for row in table.find_all('tr')[1:]:
        # Extract city name, latitude, and longitude from each row
        columns = row.find_all('td')

        name = columns[0].text.strip()
        pop = columns[1].text.strip()

        largest_cities[name] = pop





# URL of the website containing the table
url = 'https://geokeo.com/database/town/gb/'
add_on = ""

counter = 0

with open('top_100_cities_gb.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['City', 'Latitude', 'Longitude'])
    
    for i in range(2,86):
        print(i, counter)
        
        response = requests.get(url + add_on + "/")

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            table = soup.find('table')

            for row in table.find_all('tr')[1:]:
                columns = row.find_all('td')

                name = columns[1].text.strip()
                country = columns[2].text.strip()
                latitude = columns[3].text.strip()
                longitude = columns[4].text.strip()

                if name in largest_cities and country in ["England", "Wales", "Scotland"]:
                    counter += 1
                    writer.writerow([name, latitude, longitude])

        add_on = str(i)