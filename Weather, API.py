import requests

api_key = "a3bac5dd91522db92220dd99993f0499"
city = str(input("Напиши здесь название города: "))
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp'] - 273.15
    print(f'Погода в {city}: {weather_description}, Temperature: {temperature}°C')
else:
    print("Failed to retrieve data")