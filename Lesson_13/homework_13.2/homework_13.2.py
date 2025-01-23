import json
from pathlib import Path
import logging

# Змінна для лог-файлу
log_file = "json_hubernatorova.log"

# Налаштування логера
logging.basicConfig(
    filename=log_file,
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode='w'
)

# Шлях до папки з файлами з використанням абсолютного шляху
# folder_path = "/Users/nataliiahubernatorova/Desktop/QA_Automation/Lesson_13/homework_13.2/Jsons"
# directory_path = Path(folder_path)

# Шлях до папки з файлами відносно місця розташування скрипта
folder_path = Path(__file__).parent / "Jsons"
directory_path = folder_path

# Перевіряємо, чи існує папка
if not directory_path.exists():
    logging.error(f"Directory not found: {folder_path}")
    print("Папка не знайдена.")
else:
    # Проходимося по всіх файлах у папці
    for file_path in directory_path.iterdir():
        if file_path.is_file():
            try:
                # Відкриваємо файл і перевіряємо його як JSON
                with file_path.open('r', encoding='utf-8') as f:
                    json.load(f)
            except (json.JSONDecodeError, UnicodeDecodeError) as e:
                logging.error(f"File {file_path.name} is not valid JSON: {e}")
                print(f"Файл {file_path.name} є невалідним JSON.")
            except Exception as e:
                logging.error(f"Unexpected error with file {file_path.name}: {e}")
                print(f"Неочікувана помилка з файлом {file_path.name}: {e}")
        else:
            print(f"{file_path.name} - це не файл, пропускаємо.")