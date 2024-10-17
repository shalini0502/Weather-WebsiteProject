from flask import Flask, render_template, g, request
import sqlite3
from data_processing import setup_database, store_daily_summary
import requests  # Ensure you have this imported for API calls

app = Flask(__name__)
setup_database()

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('weather.db', timeout=10)  # Set timeout
    return g.db

@app.teardown_appcontext
def close_db(error):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def fetch_weather_data(city):
    api_key = '8025e3ab130522419b472280ddc6374c' # Replace with your actual OpenWeather API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"  # Using metric for °C
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

@app.route('/weather', methods=['GET', 'POST'])
def index():
    weather_data = []
    if request.method == 'POST':
        city = request.form['city']
        weather_info = fetch_weather_data(city)
        
        if weather_info:
            date = "2024-10-17"  # You might want to get the current date
            avg_temp = weather_info['main']['temp']
            min_temp = weather_info['main']['temp_min']
            max_temp = weather_info['main']['temp_max']
            condition = weather_info['weather'][0]['description']
            
            store_daily_summary(city, date, avg_temp, min_temp, max_temp, condition)
        
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM weather_summary")
        weather_data = cursor.fetchall()
    
    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
