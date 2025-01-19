import requests

# Замените эти значения своими данными
RAPIDAPI_KEY = 'YOUR_RAPIDAPI_KEY'  # Ваш RapidAPI ключ

# Получение информации о манге по названию
def get_manga_info(manga_title):
    url = "https://mangapi3.pierre.carcellermeunier.com/manga"
    headers = {
        "X-RapidAPI-Host": "mangapi3.pierre.carcellermeunier.com",
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "Content-Type": "application/json"
    }
    querystring = {"title": manga_title}

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        return response.json()
    else:
        print("Ошибка при получении данных:", response.status_code, response.text)
        return None

# Основная функция
def main():
    manga_title = input("Введите название манги: ")
    manga_info = get_manga_info(manga_title)

    if manga_info:
        print("Информация о манге:")
        print(f"Название: {manga_info.get('title')}")
        print(f"Автор: {manga_info.get('author')}")
        print(f"Статус: {manga_info.get('status')}")
        print(f"Описание: {manga_info.get('description')}")
        print(f"Жанры: {', '.join(manga_info.get('genres', []))}")
    else:
        print("Не удалось получить информацию о манге.")

if __name__ == "__main__":
    main()
