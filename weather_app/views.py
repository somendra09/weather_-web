from django.shortcuts import render
import requests
import datetime

def index(request):
    weather_data = {}
    error = None
    api_key = "cca1ab88bb98e31673f9cd8418c3cc0e"

    current_time = datetime.datetime.now().strftime('%A, %d %B %Y, %I:%M %p')

    if request.method == 'POST':
        city = request.POST.get('city')
        if city:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                weather_type = data['weather'][0]['main'].lower()

                mood_map = {
                    'clear': ('Feeling Bright ☀️', 'Shine like the sun!'),
                    'rain': ('Rainy Vibes 🌧️', 'Let the rain wash away the stress.'),
                    'clouds': ('Chill Mood ☁️', 'Behind every cloud is a rainbow.'),
                    'snow': ('Frozen Thoughts ❄️', 'Snowflakes are kisses from heaven.'),
                    'thunderstorm': ('Stormy ⚡', 'Even storms pass. Stay strong.'),
                    'mist': ('Moody Mist 🌫️', 'Breathe in the calmness.'),
                    'drizzle': ('Light Rain 🌦️', 'Drizzles bring calm to chaos.'),
                    'fog': ('Low Visibility 🌁', 'Keep moving, even if it’s unclear.')
                }

                mood, quote = mood_map.get(weather_type, ('Weather Pro', 'Stay prepared, stay awesome!'))

                weather_data = {
                    'city': data['name'],
                    'country': data['sys']['country'],
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'].title(),
                    'icon': data['weather'][0]['icon'],
                    'humidity': data['main']['humidity'],
                    'pressure': data['main']['pressure'],
                    'time': current_time,
                    'weather_type': weather_type,
                    'mood': mood,
                    'quote': quote,
                }
            else:
                error = "City not found. Please try again."

    return render(request, 'weather/index.html', {
        'weather_data': weather_data,
        'error': error,
    })
