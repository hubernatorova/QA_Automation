"""
Є відкритий API NASA який дозволяє за певними параметрами отримати дані у вигляді JSON про фото зроблені ровером
“Curiosity” на Марсі. Серед цих даних є посилання на фото які потрібно розпарсити й потім за допомогою додаткових
 запитів стягнути й зберегти ці фото як локальні файли mars_photo1.jpg, mars_photo2.jpg. Завдання потрібно зробити
 використовуючи модуль requests
 """

import requests

# URL для отримання фото з ровера Curiosity
url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
params = {
    "sol": 1000,  # Марсіанський день
    "camera": "fhaz",  # Камера фронтального виду
    "api_key": "DEMO_KEY"  # API ключ
}

# Отримання даних
response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()
    photos = data.get("photos", [])

    # Завантажуємо фото

    index = 1  # Початковий номер для файлу

    for photo in photos:
        img_url = photo.get("img_src")  # Отримуємо URL фото
        if img_url:
            img_response = requests.get(img_url)
            if img_response.status_code == 200:
                file_name = f"mars_photo{index}.jpg"  # Формуємо ім'я файлу
                with open(file_name, "wb") as file:
                    file.write(img_response.content)
                print(f"Зображення {file_name} збережено.")
                index += 1  # Збільшуємо лічильник
            else:
                print(f"Не вдалося завантажити зображення {img_url}")

else:
    print("Помилка отримання даних від NASA API")
