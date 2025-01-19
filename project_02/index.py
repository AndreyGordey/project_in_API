import requests

# Замените эти значения своими данными
API_KEY = 'YOUR_API_KEY'  # Ваш API ключ
API_SECRET = 'YOUR_API_SECRET'  # Ваш API секрет

# Получение токена доступа
def get_access_token(api_key, api_secret):
    url = 'https://api.petfinder.com/v2/oauth2/token'
    payload = {
        'grant_type': 'client_credentials',
        'client_id': api_key,
        'client_secret': api_secret
    }
    
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        return response.json()['access_token']
    else:
        print("Ошибка при получении токена:", response.json())
        return None

# Получение списка животных
def get_animals(access_token):
    url = 'https://api.petfinder.com/v2/animals'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()['animals']
    else:
        print("Ошибка при получении животных:", response.json())
        return []

# Основная функция
def main():
    access_token = get_access_token(API_KEY, API_SECRET)
    
    if access_token:
        animals = get_animals(access_token)
        
        if animals:
            print("Список доступных животных:")
            for animal in animals:
                print(f"{animal['name']} - {animal['species']} ({animal['breed']['primary']})")
        else:
            print("Нет доступных животных.")
    else:
        print("Не удалось получить токен доступа.")

if __name__ == "__main__":
    main()
