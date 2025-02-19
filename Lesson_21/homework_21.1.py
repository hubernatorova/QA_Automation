import logging
from datetime import datetime, timedelta

log_filename = "heartbeat.log"

# Налаштування логера
logging.basicConfig(
    filename=log_filename,
    level=logging.WARNING,  # Записуємо тільки WARNING і ERROR
    filemode="w",  # Перезаписуємо файл при кожному запуску
    format="%(asctime)s - %(levelname)s - %(message)s",  # Додаємо timestamp логування
    datefmt="%Y-%m-%d %H:%M:%S",
)


def analyze_heartbeat_log(input_file="hblog.txt", key="Key TSTFEED0300|7E3E|0400"):
    filtered_log = []

    # Читаємо вхідний файл і фільтруємо потрібні рядки
    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            if key in line:
                filtered_log.append(line.strip())


    # Перевіряємо, чи є достатньо рядків для аналізу
    if len(filtered_log) < 2:
        print("Недостатньо даних для аналізу.")
        return

    # Аналізуємо часові мітки
    for i in range(len(filtered_log) - 1):
        line1 = filtered_log[i]
        line2 = filtered_log[i + 1]

        # Витягуємо Timestamp
        t1_index = line1.find("Timestamp ")
        t2_index = line2.find("Timestamp ")

        if t1_index == -1 or t2_index == -1:
            logging.error(f"Invalid log format: {line1} OR {line2}")
            continue  # Пропускаємо некоректні рядки

        t1_str = line1[t1_index + 10: t1_index + 18]
        t2_str = line2[t2_index + 10: t2_index + 18]

        try:
            # Перетворюємо в datetime
            t1 = datetime.strptime(t1_str, "%H:%M:%S")
            t2 = datetime.strptime(t2_str, "%H:%M:%S")

            # Облік переходу через північ
            if t1 < t2:
                t1 += timedelta(days=1)

            # Обчислюємо різницю у секундах
            heartbeat = (t1 - t2).total_seconds()


            # Логуємо проблеми з урахуванням часу події
            if 31 <= heartbeat < 33:
                logging.warning(f"Heartbeat delay {heartbeat} sec at {t1_str}")
            elif heartbeat >= 33:
                logging.error(f"Heartbeat delay {heartbeat} sec at {t1_str}")

        except ValueError:
            logging.error(f"Invalid timestamp format in log: {line1}")

    print(f"Результат аналізу серцебиття знаходиться в файлі {log_filename}")


# Виклик функції
analyze_heartbeat_log()
