import requests

def get_weather_data(city):
    base_url = f"https://www.metaweather.com/api/location/search/?query={city}"
    
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        if data:
            woeid = data[0]["woeid"]
            weather_url = f"https://www.metaweather.com/api/location/{woeid}/"
            weather_response = requests.get(weather_url)
            if weather_response.status_code == 200:
                weather_data = weather_response.json()
                consolidated_weather = weather_data["consolidated_weather"]
                for day_weather in consolidated_weather:
                    weather_state = day_weather["weather_state_name"]
                    min_temp = day_weather["min_temp"]
                    max_temp = day_weather["max_temp"]
                    print(f"Weather in {city}: {weather_state}")
                    print(f"Min Temperature: {min_temp}°C")
                    print(f"Max Temperature: {max_temp}°C")
                    print()
            else:
                print("Failed to fetch weather data.")
        else:
            print("City not found.")
    else:
        print("Failed to fetch weather data.")

# Example usage
city = input("Enter the city name: ")
get_weather_data(city)
