import requests
import sqlite3
from datetime import datetime
from flask import g
API_KEY = '8025e3ab130522419b472280ddc6374c'  # Replace with your actual API key
CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]

# Function to set up the weather_summary table
def setup_database():
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS weather_summary
                      (city TEXT, date TEXT, avg_temp REAL, min_temp REAL, max_temp REAL, condition TEXT)''')
    conn.commit()
    conn.close()

# Convert Kelvin to Celsius
def kelvin_to_celsius(temp_k):
    return temp_k - 273.15

# Function to store weather data in the database
def store_daily_summary(city, date, avg_temp, min_temp, max_temp, condition):
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO weather_summary VALUES (?, ?, ?, ?, ?, ?)", 
                   (city, date, avg_temp, min_temp, max_temp, condition))
    conn.commit()
    print(f"Data inserted for {city} on {date}")  # Feedback for successful insertion
    conn.close()

# Function to get weather data from OpenWeatherMap API
def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    weather_data = response.json()
    print(f"Weather data for {city}: {weather_data}")  # Add this line
    return weather_data
def check_database_contents():
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM weather_summary")
    rows = cursor.fetchall()
    print("Database contents:")
    for row in rows:
        print(row)
    conn.close()
# Main function to fetch data for all cities and store it in the database
def collect_weather_data():
    for city in CITIES:
        weather_data = get_weather_data(city)
        if 'main' in weather_data:  # Ensure that the response contains valid weather data
            avg_temp = kelvin_to_celsius(weather_data['main']['temp'])
            min_temp = kelvin_to_celsius(weather_data['main']['temp_min'])
            max_temp = kelvin_to_celsius(weather_data['main']['temp_max'])
            condition = weather_data['weather'][0]['main']
            date = datetime.now().strftime('%Y-%m-%d')
            store_daily_summary(city, date, avg_temp, min_temp, max_temp, condition)
            print(f"Weather data for {city} stored.")
        else:
            print(f"Error fetching data for {city}: {weather_data}")
    check_database_contents()        

if __name__ == "__main__":
    setup_database()
    collect_weather_data()
