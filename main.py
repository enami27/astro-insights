from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.chart import Chart
import requests


# create birth chart
def create_birth_chart(date, time, location):
    # Assuming date is in 'YYYY/MM/DD', time in 'HH:MM', location as 'City, Country'
    birth_datetime = Datetime(date, time)
    birth_location = GeoPos('latitude', 'longitude')  # Get lat/long from location
    return Chart(birth_datetime, birth_location)

# simple birthchart analysis/test
def analyze_chart(chart):
    # Example: Analyze sun sign
    sun_sign = chart.getObject('Sun').sign
    return f"The sun sign is {sun_sign}."

# main
def main():
    # user data
    date = input("Enter your birth date (YYYY/MM/DD): ")
    time = input("Enter your birth time (HH:MM): ")
    location = input("Enter your birth location (City, Country): ")
    
    # create and analyze user chart
    chart = create_birth_chart(date, time, location)
    analysis = analyze_chart(chart)
    
    # display result
    print(analysis)

if __name__ == "__main__":
    main()
