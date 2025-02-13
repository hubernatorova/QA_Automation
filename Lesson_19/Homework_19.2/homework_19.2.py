"""
********** Read me ********
Для перевірки виконання завдання треба спочатку запустити файл app.py, щоб піднявся сервер, а потім запустити код
з цього файла. Шлях до файла, що завантажуємо на сервер, необхідно передати свій. Як зразок:
"/Users/nataliiahubernatorova/Desktop/QA_Automation/Lesson_19/Homework_19.1/mars_photo1.jpg"
"""

import requests
import os


def process_image(image_path):
    """Завантажує зображення, отримує посилання на нього і видаляє з сервера"""
    url = "http://127.0.0.1:8080"

    if not os.path.exists(image_path):
        print(f"❌ File not found: {image_path}")
        return {"error": "File not found"}

    print(f"📤 Завантажуємо файл: {image_path}")

    # 1. Завантаження зображення
    with open(image_path, 'rb') as image:
        files = {'image': (os.path.basename(image_path), image, 'image/jpeg')}
        response = requests.post(f"{url}/upload", files=files)

    print(f"🔄 Відповідь сервера: {response.status_code} {response.text}")

    if not str(response.status_code).startswith("2"):
        return {"error": f"Upload failed: {response.text}"}

    image_url = response.json().get("image_url")
    filename = os.path.basename(image_url)

    print(f"✅ Файл завантажено, URL: {image_url}")


    # 2. Отримання URL зображення
    response = requests.get(f"{url}/image/{filename}", headers={"Content-Type": "text"})
    if not str(response.status_code).startswith("2"):
        return {"error": f"Failed to get image URL: {response.text}"}

    print(f"🔗 Отримано URL зображення: {response.json()}")

    # 3. Видалення зображення
    response = requests.delete(f"{url}/delete/{filename}")
    if not str(response.status_code).startswith("2"):
        return {"error": f"Failed to delete image: {response.text}"}

    print(f"🗑️ Файл видалено: {filename}")

    return {"message": "Image processed successfully"}


if __name__ == '__main__':
    """Виклик методу з передачею шляху до зображення. Сюди передаємо шлях до файла. Прописала свій, як зразок"""
    image_path = "/Users/nataliiahubernatorova/Desktop/QA_Automation/Lesson_19/Homework_19.1/mars_photo1.jpg"
    result = process_image(image_path)
    print(result)
