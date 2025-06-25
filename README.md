# API-INTEGRATION-AND-DATA-VISUALIZATION

COMPANY: CODTECH IT SOLUTIONS

"NANE: SHIVAM

"INTERN ID: CT04DM932

"DOMAIN: PYTHON PROGRAMMING

"DURATION: 4 WEEEKS

*NENTOR: NEELA SANTOSH

🌐 API Integration and Data Visualization – Weather Forecast Dashboard
This project demonstrates the practical use of API integration and data visualization in Python by building a weather forecast dashboard. It utilizes the OpenWeatherMap API to retrieve real-time weather forecast data for a specific city (in this case, Delhi), processes that data, and visualizes key weather parameters such as temperature and humidity using Python libraries like Matplotlib and Seaborn.

🛠️ Key Features:
✅ Live API Integration with OpenWeatherMap.

📈 Interactive and readable graphs for temperature and humidity over time.

🌍 Easily customizable for any city by changing a single variable.

🧪 Built-in error handling to display API response status and messages.

📊 Professional data visualization using Seaborn and Matplotlib.

🧩 Project Workflow:
API Setup:

We start by integrating the OpenWeatherMap API using a personal API key.

The API endpoint returns a 5-day weather forecast with data points at 3-hour intervals.

The response is in JSON format and contains nested information about temperature, humidity, date-time, etc.

Data Extraction:

We extract three main data components: dt_txt (timestamp), main.temp (temperature), and main.humidity (humidity).

These values are stored in separate lists for plotting.

The script includes debug print statements to verify response status and contents for easier troubleshooting.

Data Visualization:

The visualization is implemented using Matplotlib and Seaborn, which are highly effective for creating publication-quality plots.

Two line plots are created on the same figure:

One for temperature (°C)

One for humidity (%)

X-axis values (timestamps) are rotated for readability, and a legend is added to differentiate between metrics.

The plot is dynamically titled based on the selected city, and layout adjustments ensure everything fits cleanly.

Error Handling:

The script checks if the key 'list' is present in the response JSON to confirm data integrity.

If the expected structure is not returned (e.g., invalid API key, city not found), the script prints a descriptive error message.

🧪 Libraries Used:
requests – to make HTTP requests to the weather API.

matplotlib.pyplot – for plotting temperature and humidity data.

seaborn – to enhance the visual appearance of the plots.

🔧 How to Run This Project:
Install Required Libraries:

bash
Copy
Edit
pip install requests matplotlib seaborn
Replace API Key:

Replace the placeholder API key (API_KEY = '267a8c7abbc6ffca5d8ff760346bf981') with your own key from https://openweathermap.org/api.

Run the Script:

bash
Copy
Edit
python weather_dashboard.py
💡 Real-World Applications:
This project simulates a simplified version of real-world dashboards used in weather monitoring systems. It serves as an excellent learning exercise for:

Beginners in API consumption and JSON parsing.

Python learners interested in data visualization and analytics.

Developers looking to integrate real-time data into Python applications.

📌 Customization Ideas:
Add more weather parameters like wind speed, pressure, and precipitation.

Convert the script into a web dashboard using Flask or Streamlit.

Implement a user input form to dynamically select any city.

Export the data and graphs as a report in PDF or PNG format.

🚀 Conclusion:
This project successfully showcases how to combine API data fetching with clean and effective data visualization to build an informative weather forecasting dashboard. It is a practical example of how data science and web integration come together in modern applications.

# OUTPUT

![Image](https://github.com/user-attachments/assets/a7d31778-cfcc-484b-9317-d9072a9a4969)

