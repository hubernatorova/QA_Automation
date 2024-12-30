# Порахувати кількість унікальних символів в строці.
# Якщо їх понад 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()

# Запитуємо в користувача введення строки
print("Введіть бажаний текст:")
string = input()

# Перетворюємо строку на множину
unique_symbols = set(string)

# Також можна перевести всі символи в нижній регістр, якщо хочемо вважати, що "А" та "а" - це один і той самий символ
# unique_symbols = set(string.lower())

# Якщо потрібно враховувати лише літери або інші конкретні символи, можна ще додати фільтрацію
# unique_symbols = set(filter(str.isalpha, string))

# Підраховуємо довжину множини
count_unique_symbols = len(unique_symbols)

if count_unique_symbols > 10:
    print(True)
else:
    print(False)



my_string = input("Enter your string: ")
print(len(set())>=10)
if len(set(my_string))>=10:
    print(True)
else:
    print(False)


lst = []
for i in my_string:
    if i not in lst:
        lst.append(i)