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

print("Enter your City name. ")
local_city_input = input(" > ")

lgitude_value, ltitude_value = convert_geocoding()
weather_code = get_weathercode()

# The chechlist :D:D:D:D::DD:D:D:D::D:D::D:D::D

if weather_code:
    if weather_code == 0:
        print(current_weather,clear_sky,searching_playlist)
        playlist_get = requests.get(f"https://api.spotify.com/v1/search?q={clear_sky}&type=playlist&market=de", headers=header_api_token).json()
        print(playlist_get["playlists"]["items"][0]["external_urls"]["spotify"])
    elif weather_code ==  1:
        print(current_weather,mainly_clear,searching_playlist)
        playlist_get = requests.get(f"https://api.spotify.com/v1/search?q={mainly_clear}&type=playlist&market=de", headers=header_api_token).json()
        print(playlist_get["playlists"]["items"][0]["external_urls"]["spotify"])
    elif weather_code == 2:
        print(current_weather,partly_cloudy,searching_playlist)
        playlist_get = requests.get(f"https://api.spotify.com/v1/search?q={partly_cloudy}&type=playlist&market=de", headers=header_api_token).json()
        print(playlist_get["playlists"]["items"][0]["external_urls"]["spotify"])
    elif weather_code == 3:
        print(current_weather,overcast,searching_playlist)
        playlist_get = requests.get(f"https://api.spotify.com/v1/search?q={overcast}&type=playlist&market=de", headers=header_api_token).json()
        print(playlist_get["playlists"]["items"][0]["external_urls"]["spotify"])
    elif weather_code == 45:
        print(current_weather,fog,searching_playlist)
        playlist_get = requests.get(f"https://api.spotify.com/v1/search?q={fog}&type=playlist&market=de", headers=header_api_token).json()
        print(playlist_get["playlists"]["items"][0]["external_urls"]["spotify"])
    elif weather_code == 48:
        print(current_weather,deposting_rime_fog,searching_playlist)
        playlist_get = requests.get(f"https://api.spotify.com/v1/search?q={deposting_rime_fog}&type=playlist&market=de", headers=header_api_token).json()
        print(playlist_get["playlists"]["items"][0]["external_urls"]["spotify"])
    elif weather_code == 51:
        print(current_weather,drizzle_light,searching_playlist)
        playlist_get = requests.get(f"https://api.spotify.com/v1/search?q={drizzle_light}&type=playlist&market=de", headers=header_api_token).json()
        print(playlist_get["playlists"]["items"][0]["external_urls"]["spotify"])
    elif weather_code == 53:
        print(current_weather,drizzle_moderate,searching_playlist)
        playlist_get = requests.get(f"https://api.spotify.com/v1/search?q={drizzle_moderate}&type=playlist&market=de", headers=header_api_token).json()
        print(playlist_get["playlists"]["items"][0]["external_urls"]["spotify"])
    elif weather_code == 55:
        print(current_weather,drizzle_dense,searching_playlist)
        playlist_get = requests.get(f"https://api.spotify.com/v1/search?q={drizzle_dense}&type=playlist&market=de", headers=header_api_token).json()
        print(playlist_get["playlists"]["items"][0]["external_urls"]["spotify"])
    elif weather_code == 56:
        print(current_weather,freezing_drizzle_light,searching_playlist)
        playlist_get = requests.get(f"https://api.spotify.com/v1/search?q={freezing_drizzle_light}&type=playlist&market=de", headers=header_api_token).json()
        print(playlist_get["playlists"]["items"][0]["external_urls"]["spotify"])
    elif weather_code == 57:
        print(current_weather,freezing_drizzle_dense,searching_playlist)
        playlist_get = requests.get(f"https://api.spotify.com/v1/search?q={freezing_drizzle_dense}&type=playlist&market=de", headers=header_api_token).json()
        print(playlist_get["playlists"]["items"][0]["external_urls"]["spotify"])
    elif weather_code == 61:
        print(current_weather,rain_slight,searching_playlist)
        playlist_get = requests.get(f"https://api.spotify.com/v1/search?q={rain_slight}&type=playlist&market=de", headers=header_api_token).json()
        print(playlist_get["playlists"]["items"][0]["external_urls"]["spotify"])
    elif weather_code == 63:
        print(current_weather,rain_moderate,searching_playlist)
        playlist_get = requests.get(f"https://api.spotify.com/v1/search?q={rain_moderate}&type=playlist&market=de", headers=header_api_token).json()
        print(playlist_get["playlists"]["items"][0]["external_urls"]["spotify"])
    elif weather_code == 65:
        print(current_weather,rain_heavy,searching_playlist)
        playlist_get = requests.get(f"https://api.spotify.com/v1/search?q={rain_heavy}&type=playlist&market=de", headers=header_api_token).json()
        print(playlist_get["playlists"]["items"][0]["external_urls"]["spotify"])
    elif weather_code == 66:
        print(current_weather,freezing_rain_light,searching_playlist)
        playlist_get = requests.get(f"https://api.spotify.com/v1/search?q={freezing_rain_light}&type=playlist&market=de", headers=header_api_token).json()
        print(playlist_get["playlists"]["items"][0]["external_urls"]["spotify"])
    elif weather_code == 67:
        print(current_weather,freezing_rain_heavy,searching_playlist)
        playlist_get = requests.get(f"https://api.spotify.com/v1/search?q={freezing_rain_heavy}&type=playlist&market=de", headers=header_api_token).json()
        print(playlist_get["playlists"]["items"][0]["external_urls"]["spotify"])
    elif weather_code == 71:
        print(current_weather,snow_fall_slight,searching_playlist)
        playlist_get = requests.get(f"https://api.spotify.com/v1/search?q={snow_fall_slight}&type=playlist&market=de", headers=header_api_token).json()
        print(playlist_get["playlists"]["items"][0]["external_urls"]["spotify"])
    elif weather_code == 73:
        print(current_weather,snow_fall_moderate,searching_playlist)
        playlist_get = requests.get(f"https://api.spotify.com/v1/search?q={snow_fall_moderate}&type=playlist&market=de", headers=header_api_token).json()
        print(playlist_get["playlists"]["items"][0]["external_urls"]["spotify"])
    elif weather_code == 75:
        print(current_weather,snow_fall_heavy,searching_playlist)
        playlist_get = requests.get(f"https://api.spotify.com/v1/search?q={snow_fall_heavy}&type=playlist&market=de", headers=header_api_token).json()
        print(playlist_get["playlists"]["items"][0]["external_urls"]["spotify"])
    elif weather_code == 77:
        print(current_weather,snow_grains,searching_playlist)
        playlist_get = requests.get(f"https://api.spotify.com/v1/search?q={snow_grains}&type=playlist&market=de", headers=header_api_token).json()
        print(playlist_get["playlists"]["items"][0]["external_urls"]["spotify"])
    elif weather_code == 80:
        print(current_weather,rain_showers_slight,searching_playlist)
        playlist_get = requests.get(f"https://api.spotify.com/v1/search?q={rain_showers_slight}&type=playlist&market=de", headers=header_api_token).json()
        print(playlist_get["playlists"]["items"][0]["external_urls"]["spotify"])
    elif weather_code == 81:
        print(current_weather,rain_showers_moderate,searching_playlist)
        playlist_get = requests.get(f"https://api.spotify.com/v1/search?q={rain_showers_moderate}&type=playlist&market=de", headers=header_api_token).json()
        print(playlist_get["playlists"]["items"][0]["external_urls"]["spotify"])
    elif weather_code == 82:
        print(current_weather,rain_showers_violent,searching_playlist)
        playlist_get = requests.get(f"https://api.spotify.com/v1/search?q={rain_showers_violent}&type=playlist&market=de", headers=header_api_token).json()
        print(playlist_get["playlists"]["items"][0]["external_urls"]["spotify"])
    elif weather_code == 85:
        print(current_weather,snow_showers_slight,searching_playlist)
        playlist_get = requests.get(f"https://api.spotify.com/v1/search?q={snow_showers_slight}&type=playlist&market=de", headers=header_api_token).json()
        print(playlist_get["playlists"]["items"][0]["external_urls"]["spotify"])
    elif weather_code == 86:
        print(current_weather,snow_showers_heavy,searching_playlist)
        playlist_get = requests.get(f"https://api.spotify.com/v1/search?q={snow_showers_heavy}&type=playlist&market=de", headers=header_api_token).json()
        print(playlist_get["playlists"]["items"][0]["external_urls"]["spotify"])
    elif weather_code == 95:
        print(current_weather,thunderstorm,searching_playlist)
        playlist_get = requests.get(f"https://api.spotify.com/v1/search?q={thunderstorm}&type=playlist&market=de", headers=header_api_token).json()
        print(playlist_get["playlists"]["items"][0]["external_urls"]["spotify"])
    elif weather_code == 96:
        print(current_weather,thunderstorm_with_slight_hail,searching_playlist)
        playlist_get = requests.get(f"https://api.spotify.com/v1/search?q={thunderstorm_with_slight_hail}&type=playlist&market=de", headers=header_api_token).json()
        print(playlist_get["playlists"]["items"][0]["external_urls"]["spotify"])
    elif weather_code == 99:
        print(current_weather,thunderstorm_with_heavy_hail,searching_playlist)
        playlist_get = requests.get(f"https://api.spotify.com/v1/search?q={thunderstorm_with_heavy_hail}&type=playlist&market=de", headers=header_api_token).json()
        print(playlist_get["playlists"]["items"][0]["external_urls"]["spotify"])



