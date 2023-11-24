from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.chart import Chart
from flatlib.const import ASC, MC
import requests

# Function to get latitude and longitude from location using Nominatim
def get_lat_long(location):
    base_url = 'https://nominatim.openstreetmap.org/search'
    params = {'q': location, 'format': 'json'}
    response = requests.get(base_url, params=params)
    data = response.json()

    if data:
        latitude = float(data[0]['lat'])  # Convert latitude to float
        longitude = float(data[0]['lon'])  # Convert longitude to float
        return latitude, longitude
    else:
        raise ValueError("Could not find the location")


# Modified function to create a birth chart
def create_birth_chart(date, time, location):
    birth_datetime = Datetime(date, time)
    
    # Retrieve latitude and longitude from location
    latitude, longitude = get_lat_long(location)
    birth_location = GeoPos(latitude, longitude)

    chart = Chart(birth_datetime, birth_location)

    # Retrieve ASC and MC
    ascendant = chart.get(ASC)
    midheaven = chart.get(MC)

    return chart, ascendant, midheaven

# Simple birthchart analysis/test
def analyze_chart(chart):
    for obj in chart.objects:
        print(obj)

# retrieve chart houses
def chart_houses(chart):
    for house in chart.houses:
        print(house)

# check whether the chart is day or night
def is_diurnal(chart):
    if(chart.isDiurnal() == True):
        print("You have a day chart")
    else:
        print("You have a night chart")

# get moon phase for a given chart
def get_moon_phase(chart):
    print("The moon was in " + chart.getMoonPhase() + " when you were born.")

# Main

def main():
    try:
        # User data
        name = input("Enter your name : ")
        date = input("Enter your birth date (YYYY/MM/DD): ")
        time = input("Enter your birth time (HH:MM): ")
        location = input("Enter your birth location (City, Country): ")
        
        # Create chart and retrieve ASC and MC
        chart, ascendant, midheaven = create_birth_chart(date, time, location)

        # Ask for user choice after getting birth details
        choice = input("Enter '1' to view your chart analysis, or '2' to view your chart houses, or 3 for other chart properties: ")

        if choice == '1':
            # If chart analysis is chosen
            print(f"Hello {name}, here's your chart analysis!")
            analyze_chart(chart)
            print(f"Ascendant (ASC): {ascendant}")
            print(f"Midheaven (MC): {midheaven}")
        elif choice == '2':
            # View chart houses
            print(f"Hello {name}, here are the sign for each one of your houses")
            chart_houses(chart)
        elif choice == '3':
            get_moon_phase(chart)
            is_diurnal(chart)
        else:
            print("Invalid choice.")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
