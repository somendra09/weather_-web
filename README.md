# 🌤️ Weather Pro Django Web App

**Weather Pro** is a beautiful and responsive Django web application that provides real-time weather updates using the OpenWeatherMap API. It also includes dynamic YouTube music suggestions based on current weather mood

---

## 🚀 Features

- 🌍 Get weather info by city or current location (Geolocation)
- 🌤️ Real-time weather data (temperature, humidity, pressure, icon, etc.)
- 🧠 Suggestive quote and mood based on weather
- 👕 Outfit suggestion based on temperature
- 🎵 YouTube music recommendation based on weather type (Rain, Clear, Cloudy)
- 🧊 Clean UI with glassmorphism effect
- 📱 Fully responsive design

---

## 🔧 Tech Stack

- **Backend:** Django 5.2
- **Frontend:** HTML, CSS, Bootstrap 5
- **API:** OpenWeatherMap
- **Language:** Python 3.13

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/somendra09/weather_-web.git
cd weather_-web

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

# Run server
python manage.py runserver


🔑 API Key Setup
Go to OpenWeatherMap and get your API key.

In views.py, paste your API key in place of:

python
Copy
Edit
api_key = "your_api_key_here"


