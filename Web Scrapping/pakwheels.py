from bs4 import BeautifulSoup
import requests
import csv

base_url = 'https://www.pakwheels.com/used-cars/karachi/24857'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' +
                  'AppleWebKit/537.36 (KHTML, like Gecko) ' +
                  'Chrome/115.0.0.0 Safari/537.36'
}

#  CSV file
with open("pakwheels_paginated.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow([
        "Car Title", "Car Price", "Car Location", "Car Year",
        "Car Km", "Car Fuel", "Car CC", "Car Transmission"
    ])

    #  Loop through first 5 pages (you can increase)
    for page in range(1, 6):  # page 1 to 5
        print(f"Scraping page {page}...")
        url = f"{base_url}?page={page}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        cars = soup.find_all("li", class_="classified-listing")

        for car in cars:
            try:
                Car_title = car.find("div", class_="name-price").find("h3").text.strip()
                Car_price = car.find("div", class_="name-price").find("div", class_="price-details").text.strip()
                
                car_info = car.find("div", class_="col-md-12 grid-date")
                uls = car_info.find_all("ul")

                car_location = uls[0].find("li").text.strip() if len(uls) > 0 else "N/A"
                details = uls[1].find_all("li") if len(uls) > 1 else []

                car_year = details[0].text.strip() if len(details) > 0 else "N/A"
                car_Km = details[1].text.strip() if len(details) > 1 else "N/A"
                car_fuel = details[2].text.strip() if len(details) > 2 else "N/A"
                car_CC = details[3].text.strip() if len(details) > 3 else "N/A"
                car_transmission = details[4].text.strip() if len(details) > 4 else "N/A"

                writer.writerow([
                    Car_title, Car_price, car_location, car_year,
                    car_Km, car_fuel, car_CC, car_transmission
                ])
            except Exception as e:
                print(" Error:", e)

print(" All paginated car data saved successfully!")
