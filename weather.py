from dotenv import load_dotenv
import os
import requests

load_dotenv(".env", override=True)
api_key = os.getenv("OPENWEATHER_API_KEY")

print("Welcome to Weather App")
city = input("Enter city name: ").strip()

if not api_key:
    print("API key not found. Check your .env file.")
else:
    try:
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {"q": city, "appid": api_key, "units": "metric"}
        response = requests.get(url, params=params, timeout=10)
        print("Status code:", response.status_code)

        if response.status_code == 200:
            data = response.json()
            print("\nCurrent Weather")
            print("City:", data["name"])
            print("Temperature:", data["main"]["temp"], "°C")
            print("Humidity:", data["main"]["humidity"], "%")
            print("Weather:", data["weather"][0]["description"].title())

            forecast_url = "https://api.openweathermap.org/data/2.5/forecast"
            forecast_params = {"q": city, "appid": api_key, "units": "metric"}
            forecast_response = requests.get(
                forecast_url, params=forecast_params, timeout=10
            )

            if forecast_response.status_code == 200:
                forecast_data = forecast_response.json()
                print("\n5-Day Weather Forecast")
                displayed_dates = set()

                for item in forecast_data["list"]:
                    forecast_date = item["dt_txt"][:10]

                    if forecast_date not in displayed_dates:
                        print("\nDate:", forecast_date)
                        print("Temperature:", item["main"]["temp"], "°C")
                        print("Weather:", item["weather"][0]["description"].title())
                        displayed_dates.add(forecast_date)
            else:
                print("Could not fetch the weather forecast.")
                print("Status code:", forecast_response.status_code)

        elif response.status_code == 404:
            print("City not found. Please check the spelling.")
        elif response.status_code == 401:
            print("Invalid API key. Check your OpenWeather API key.")
        else:
            print("Could not fetch current weather.")
            print(response.text)

    except requests.exceptions.Timeout:
        print("The request took too long. Please try again.")
    except requests.exceptions.ConnectionError:
        print("No internet connection. Please check your network.")
    except requests.exceptions.RequestException as error:
        print("An error occurred:", error)

