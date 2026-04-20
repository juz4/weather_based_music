# Imports

import requests
import json

# Spotify api key

url = "https://accounts.spotify.com/api/token"

with open("config.json") as file:
    load_clients = json.load(file)
    client_id = load_clients["client_keys"][0]["client_id"]
    client_secret = load_clients["client_keys"][1]["client_secret"]

body = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret
}

header_content_type = {
    "Content-Type": "application/x-www-form-urlencoded"
}

access_token_gen = requests.post(url, headers=header_content_type, data=body).json()
api_token = access_token_gen["access_token"]

header_api_token = {
    "Authorization": f"Bearer {api_token}"
}

# Weather variable documentation
# WMO Weather interpretation codes (WW)

clear_sky = "clear sky"
mainly_clear = "mainly clear"
partly_cloudy = "partly cloudy" 
overcast = "overcast"
fog = "fog"
deposting_rime_fog = "depositing rime fog"
drizzle_light = "drizzle: Light"
drizzle_moderate = "drizzle: moderate"
drizzle_dense = "drizzle: dense intensity"
freezing_drizzle_light = "freezing drizzle: light intensity"
freezing_drizzle_dense = "freezing drizzle: dense intensity"
rain_slight = "rain: slight intensity"
rain_moderate = "rain: moderate intensity"
rain_heavy = "rain: heavy intensity"
freezing_rain_light = "freezing rain: light intensity"
freezing_rain_heavy = "freezing rain: heavy intensity"
snow_fall_slight = "snow fall: slight intensity"
snow_fall_moderate = "snow fall: moderate intensity"
snow_fall_heavy = "snow fall: heavy intensity"
snow_grains = "snow grains"
rain_showers_slight = "slight rain showers"
rain_showers_moderate = "moderated rain showers"
rain_showers_violent = "violent rain showers"
snow_showers_slight = "slight snow shower"
snow_showers_heavy = "heavy snow shower"
thunderstorm = "thunderstorm"
thunderstorm_with_slight_hail = "thunderstorm with slight hail"
thunderstorm_with_heavy_hail = "thudnerstorm with heavy hail"

# Copyprint

current_weather = "Currently, the weather state in the selected city is" # Who do I look like that I write the same sentence over and over again XD
searching_playlist = " \nSearching now for a playlist."

# Functions

def convert_geocoding():
    request_weather_informations = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={local_city_input}&count=1&id=1").json()
    longitude = request_weather_informations["results"][0]["longitude"]
    latitude = request_weather_informations["results"][0]["latitude"]
    
    return longitude, latitude

def get_weathercode():
    request_weathercode = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={ltitude_value}&longitude={lgitude_value}&current=weather_code&forecast_days=1").json()
    weather_code = request_weathercode["current"]["weather_code"]

    return weather_code

def get_weatherstate():
    if weather_code == 0:
        weather_state = clear_sky
    elif weather_code == 1:
        weather_state = mainly_clear
    elif weather_code == 2:
        weather_state = partly_cloudy
    elif weather_code == 3:
        weather_state = overcast
    elif weather_code == 45:
        weather_state = fog
    elif weather_code == 48:
        weather_state = deposting_rime_fog
    elif weather_code == 51:
        weather_state = drizzle_light
    elif weather_code == 53:
        weather_state = drizzle_moderate
    elif weather_code == 55:
        weather_state = drizzle_dense
    elif weather_code == 56:
        weather_state = freezing_drizzle_light
    elif weather_code == 57:
        weather_state = freezing_drizzle_dense
    elif weather_code == 61:
        weather_state = rain_slight
    elif weather_code == 63:
        weather_state = rain_moderate
    elif weather_code == 65:
        weather_state = rain_heavy
    elif weather_code == 66:
        weather_state = freezing_rain_light
    elif weather_code == 67:
        weather_state = freezing_rain_heavy
    elif weather_code == 71:
        weather_state = snow_fall_slight
    elif weather_code == 73:
        weather_state = snow_fall_moderate
    elif weather_code == 75:
        weather_state = snow_fall_heavy
    elif weather_code == 77:
        weather_state = snow_grains
    elif weather_code == 80:
        weather_state = rain_showers_slight
    elif weather_code == 81:
        weather_state = rain_showers_moderate
    elif weather_code == 82:
        weather_state = rain_showers_violent
    elif weather_code == 85:
        weather_state = snow_showers_slight
    elif weather_code == 86:
        weather_state = snow_showers_heavy
    elif weather_code == 95:
        weather_state = thunderstorm
    elif weather_code == 96:
        weather_state = thunderstorm_with_slight_hail
    elif weather_code == 99:
        weather_state = thunderstorm_with_heavy_hail

    return weather_state

# User variable inputs

print("Enter your City name. ")
local_city_input = input(" > ")

lgitude_value, ltitude_value = convert_geocoding()
weather_code = get_weathercode()
local_city_weather_state = get_weatherstate()

print(f"The current state of the city you've entered in is {local_city_weather_state}.\nLooking for matching playlist...")
input("Press ENTER to get the link matching to the weather.\n")
playlist_get = requests.get(f"https://api.spotify.com/v1/search?q={local_city_weather_state}&type=playlist&market=de", headers=header_api_token).json()
print(playlist_get["playlists"]["items"][0]["external_urls"]["spotify"])
