import matplotlib.pyplot as plt

def visualize_weather(city, dates, temps):
    plt.plot(dates, temps, label=city)
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title(f'Temperature Trend in {city}')
    plt.legend()
    plt.show()
