import requests
import matplotlib.pyplot as plt
import seaborn as sns

# 🔑 Replace with your real API key
API_KEY = '267a8c7abbc6ffca5d8ff760346bf981'
CITY = 'Delhi'
URL = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

# Fetch data
response = requests.get(URL)
data = response.json()

# Debug output
print("Status Code:", response.status_code)
print("API Response:")
print(data)  # See what the API is actually returning

# Only proceed if successful
if 'list' in data:
    # Extract weather data
    dates = []
    temps = []
    humidities = []

    for item in data['list']:
        dates.append(item['dt_txt'])
        temps.append(item['main']['temp'])
        humidities.append(item['main']['humidity'])

    # Create graph
    plt.figure(figsize=(14, 6))
    sns.lineplot(x=dates, y=temps, marker='o', label='Temperature (°C)')
    sns.lineplot(x=dates, y=humidities, marker='s', label='Humidity (%)')
    plt.xticks(rotation=45)
    plt.title(f"5-Day Weather Forecast for {CITY}")
    plt.xlabel("Date-Time")
    plt.ylabel("Values")
    plt.legend()
    plt.tight_layout()
    plt.show()

else:
    print("❌ Error: API did not return expected data.")
    if "message" in data:
        print("Reason:", data["message"])
