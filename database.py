import sqlite3
from datetime import datetime

# Create SQLite connection and weather table
def setup_database():
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS weather_summary
                      (city TEXT, date TEXT, avg_temp REAL, min_temp REAL, max_temp REAL, condition TEXT)''')
    conn.commit()
    return conn

def store_daily_summary(city, date, avg_temp, min_temp, max_temp, condition):
    conn = setup_database()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO weather_summary VALUES (?, ?, ?, ?, ?, ?)", 
                   (city, date, avg_temp, min_temp, max_temp, condition))
    conn.commit()
    print(f"Data inserted for {city} on {date}") 
    conn.close()

# Calculate daily summary
def calculate_daily_summary(weather_data_list):
    avg_temp = sum([kelvin_to_celsius(data['main']['temp']) for data in weather_data_list]) / len(weather_data_list)
    min_temp = min([kelvin_to_celsius(data['main']['temp']) for data in weather_data_list])
    max_temp = max([kelvin_to_celsius(data['main']['temp']) for data in weather_data_list])
    dominant_condition = max(set([data['weather'][0]['main'] for data in weather_data_list]), 
                             key=[data['weather'][0]['main'] for data in weather_data_list].count)
    return avg_temp, min_temp, max_temp, dominant_condition
