import csv

# Визначаємо імена файлів
file1 = "random.csv"
file2 = "random-michaels.csv"
output_file = "result_hubernatorova.csv"

# Множина для унікальних рядків
unique_rows = set()

with open(file1, 'r', newline='', encoding='utf-8') as f1, open(file2, 'r', newline='', encoding='utf-8') as f2:
    reader1 = csv.reader(f1)
    reader2 = csv.reader(f2)

    # Зчитуємо заголовки
    header1 = next(reader1)
    header2 = next(reader2)

    # Перевірка відповідності заголовків
    if header1 != header2:
        raise ValueError(f"Заголовки у файлах не співпадають:\n{file1}: {header1}\n{file2}: {header2}")

    # Додавання рядків до множини
    for row in reader1:
        unique_rows.add(tuple(row))  # Додаємо як tuple для унікальності

    for row in reader2:
        unique_rows.add(tuple(row))

# Запис результатів у новий файл
with open(output_file, 'w', newline='', encoding='utf-8') as f_out:
    writer = csv.writer(f_out)
    # Записуємо заголовок
    writer.writerow(header1)
    for row in unique_rows:
        writer.writerow(row)

print(f"Результат збережено у файл {output_file}")
