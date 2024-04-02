import requests
from generate_response import  text_to_speech
from playing_audio import  play_audio

def get_weather(api_key, city):
    api_key = "5f38ab307a314fff97144906243003"

    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        weather = data['current']["temp_c"]
        
        return weather
    else:
        print("Error fetching weather data:", response.status_code)
        return None

# Example usage:
city = "Cairo"
api_key = "5f38ab307a314fff97144906243003"
weather = get_weather(api_key, city)
if weather:
    play_audio(text_to_speech(f"درجة الحرارة الان هي {weather} سيليزياس"))