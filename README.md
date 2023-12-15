# Astro insights

## Description
This app provides a comprehensive and easy to grasp astrology analysis using birthdate, time and location. It features multiple functionalities like analyzing chart objects (planets, houses...), identifying chart houses and determining whether a given chart is a night or day chart, as well as finding the moon phase at the time of birth.

## Installation and usage

### Pre-requisites
- Python 3.x
- Flatlib library
- Requests library

### Installation
To install the librarues, run the following commands : 
`pip install flatlib`, `pip install requests`

Run the script and follow the on screen prompts
`python main.py` or `python3 main.py`

Enter the requested information, the script will generate a chart based on the provided info

## Features
**Birth chart creation** : Generate a birthchart using the flatlib API
**Chart analysis** : Analyzes various aspects of the astrology chart.
**Chart houses** : Retrieves and display chart houses
**Diurnal check** : Determines if the chart is a day or night chart
**Moon phase** : Finds out the moon phase at the time of birth

## How it works
**Data input** : The user inputs their birth details
**Location processing** : Uses Nominatim API to convert location to latitude and longitude
**Chart Generation** : Creates a birth chart with Flatlib using the processed data
**Analysis operations** : Provides options to view different aspects of the astrology chart
