Weather App

A Python application that fetches current weather information and a 5-day forecast using the OpenWeather API.

Features

- Search weather by city name
- Display current temperature in Celsius
- Display humidity and weather conditions
- Show a 5-day forecast
- Handle invalid city names and network errors
- Store the API key securely using an environment file

Technologies Used

- Python
- OpenWeather API
- Requests
- JSON
- Python-dotenv

Installation

1. Install Python.

2. Install the required libraries:
   
   "py -m pip install -r requirements.txt"

3. Create a ".env" file and add your OpenWeather API key:
   
   "OPENWEATHER_API_KEY=your_actual_api_key"

4. Run the application:
   
   "py weather.py"

How It Works

The application accepts a city name, sends a request to the OpenWeather API, processes the JSON response, and displays current weather information and forecast data.

Author

B.Tech Computer Science and Engineering Student