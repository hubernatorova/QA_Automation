# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сформує новий list (наприклад lst2), який містить лише змінні типу string,
# які присутні в lst1. Данні в списку можуть бути будь якими

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

# Оголошуємо порожній список, в який будем додавати елементи лише типу string
lst2 = []

# Проходимось циклом по першому списку
for i in lst1:
    if isinstance(i, str):
        lst2.append(i)

print(lst2)

for i in lst1:
    if type(i) == str:
        lst2.append(i)

print(lst2)