import requests
import sys

from datetime import datetime

api_key = '9a38bc3b54ad4e99452b9837beba912e'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

# Create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_status = api_data['weather'][0]['main']
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']

# Saving the reference of the standard output
original_stdout = sys.stdout

# All our Output gets exported to our .txt file
with open("output.txt", "w") as f:
    sys.stdout = f
    print ("-------------------------------------------------------------")
    print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
    print ("-------------------------------------------------------------")

    print ("Current temperature is: {:.2f} deg C".format(temp_city))
    print ("Current Weather Status:",weather_status)
    print ("Current weather desc  :",weather_desc)
    print ("Current Humidity      :",hmdt, '%')
    print ("Current wind speed    :",wind_spd ,'kmph')
    # Reset the standard output
    sys.stdout = original_stdout
