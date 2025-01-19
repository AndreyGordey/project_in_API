import requests
import venv
def get_weather(city, api_key):
    # URL для запроса к API OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    # Отправка GET-запроса к API
    response = requests.get(url)
    
    # Проверка успешности запроса
    if response.status_code == 200:
        data = response.json()
        # Извлечение необходимых данных
        city_name = data['name']
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        
        # Печать результатов
        print(f"Погода в городе {city_name}:")
        print(f"Температура: {temperature}°C")
        print(f"Описание: {weather_description}")
    else:
        print("Ошибка при получении данных о погоде:", response.status_code)

if __name__ == "__main__":
    # Введите свой API-ключ здесь
    api_key = "fa46cb5a3781329ffe73701682ff8fbd"
    
    # Введите название города для получения погоды
    city = input("Введите название города: ")
    
    get_weather(city, api_key)
