# Real-Time Weather Monitoring System

## Objective:
This project is a real-time weather monitoring system that retrieves weather data from the OpenWeatherMap API and provides daily weather summaries, real-time alerts, and advanced analytics based on user preferences.(Note- Go to **Master Branch**).

## Features:
1. **Real-Time Weather Retrieval:** Continuously retrieves weather data for Indian metros like Delhi, Mumbai, Chennai, etc.
2. **Daily Weather Summaries:** Aggregates daily weather data including average, max, min temperatures, and dominant weather conditions.
3. **User Preferences:** Users can set their preferred cities and temperature alert thresholds.
4. **Advanced Analytics:** Compares current weather conditions with historical trends and provides visualizations.
5. **Alerting System:** Alerts users when defined thresholds are exceeded.
6. **Historical Data Retrieval:** Allows retrieval and visualization of historical weather data.

## Design Choices:
1. **Database:** SQLite is used to store weather data and user preferences. It's lightweight and easy to integrate.
2. **API:** OpenWeatherMap API is used for weather data retrieval. Data is retrieved in real-time at configurable intervals.
3. **Web Framework:** Flask is used to create a simple web interface where users can view weather data and configure their preferences.
4. **Front-end:** Basic HTML for the interface, with future plans for integrating Chart.js for visualization.
5. **Real-Time Processing:** Weather data is processed and aggregated in real-time as it is received from the API.

## Prerequisites:
- Python 3.6+
- SQLite3
- Flask
- Requests (for API calls)

### API Key:
Sign up for a free API key from [OpenWeatherMap](https://openweathermap.org/api). You will need to replace the placeholder API key in the code.

## Installation:

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/shalini0502/weather-monitoring-system.git
    cd weather-monitoring-system
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up the Database:**
    The database setup is automatic, but you can check the `data_processing.py` file for how it's structured.

4. **Run the Application:**
    ```bash
    python app.py
    ```

5. **Access the Web Interface:**
    Open your browser and go to `http://127.0.0.1:5000/weather`.

## Usage:
- **Weather Summary:** Enter the city in the input field and submit to see the real-time weather data and summaries.
- **User Preferences:** Set your preferred cities and temperature thresholds for alerts.
- **View Historical Data:** Use the additional routes to fetch historical data.

## Future Work:
- Integration of additional weather parameters like humidity and wind speed.
- Enhanced visualizations using Chart.js or D3.js for graphical representation.
- Deployment in production using a WSGI server like Gunicorn.

## Authors:
Shalini
