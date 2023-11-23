from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.chart import Chart
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

    return Chart(birth_datetime, birth_location)

# Simple birthchart analysis/test
def analyze_chart(chart):
    sun_sign = chart.getObject('Sun').sign
    return f"The sun sign is {sun_sign}."

# Main
def main():
    try:
        # User data
        date = input("Enter your birth date (YYYY/MM/DD): ")
        time = input("Enter your birth time (HH:MM): ")
        location = input("Enter your birth location (City, Country): ")
        
        # Create and analyze user chart
        chart = create_birth_chart(date, time, location)
        analysis = analyze_chart(chart)
        
        # Display result
        print(analysis)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
