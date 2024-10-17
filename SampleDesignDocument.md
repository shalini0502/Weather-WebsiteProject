# Real-Time Weather Monitoring System: Design Document

## 1. Overview:
This document describes the architecture, data flow, and core components of the real-time weather monitoring system. The system collects weather data from the OpenWeatherMap API, processes and stores it, and provides both real-time updates and historical data to users.

## 2. System Architecture:
The system consists of the following layers:
1. **Data Retrieval Layer:** Calls the OpenWeatherMap API at regular intervals to fetch weather data for predefined cities.
2. **Data Processing Layer:** Converts temperature from Kelvin to Celsius and calculates daily weather summaries.
3. **Database Layer:** SQLite database stores weather data and user preferences.
4. **Web Layer:** Flask handles routing, form submissions, and serving HTML templates to the user.
5. **Alerting Layer:** Monitors the weather conditions in real-time and sends alerts if thresholds are exceeded.

## 3. Data Flow:
1. User enters a city and requests weather data.
2. The system fetches data from the OpenWeatherMap API and processes it.
3. Processed data is stored in the SQLite database.
4. Daily weather summaries are calculated and stored.
5. User preferences are applied to trigger real-time alerts if conditions exceed predefined thresholds.
6. Historical data is retrieved from the database and displayed.

## 4. Database Design:
### Tables:
- **weather_summary (city, date, avg_temp, min_temp, max_temp, condition)**
  - Stores the weather summary for each city on a daily basis.
- **user_preferences (user_id, preferred_city, temperature_threshold)**
  - Stores user preferences for alerts and favorite cities.

## 5. API Integration:
The system uses the OpenWeatherMap API to retrieve the following weather details:
- **Main Condition:** (Clear, Rain, etc.)
- **Temperature:** Current, minimum, and maximum temperature in °C.
- **Timestamp:** Unix timestamp for each weather update.

## 6. Core Algorithms:
1. **Temperature Conversion:** Converts temperatures from Kelvin to Celsius.
2. **Daily Aggregation:** Calculates daily average, max, and min temperatures.
3. **Alerting Mechanism:** Continuously monitors weather conditions and compares them with user-defined thresholds.

## 7. Future Enhancements:
- Extend support for more weather parameters (humidity, wind speed).
- Improve user experience with better visualizations (charts, graphs).
- Deploy the system on a production server (Heroku or AWS).

## 8. Challenges and Solutions:
- **Challenge:** Real-time processing of weather data while ensuring low latency.
  - **Solution:** Efficient API calls and local database storage to minimize processing time.
- **Challenge:** Triggering real-time alerts.
  - **Solution:** Continuous monitoring with a background scheduler to evaluate thresholds.

## 9. Conclusion:
This design ensures that the weather monitoring system is scalable, reliable, and easy to use while meeting the project's functional and non-functional requirements.

