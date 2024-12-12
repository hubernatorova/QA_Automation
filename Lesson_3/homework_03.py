"""
    # task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
    # task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
    # task 03 == Виведіть змінну alice_in_wonderland на друк
"""

alice_in_wonderland = (f"'That depends a good deal on where you want to get to,' said the Cat."
                       f"\n'I don't much care where,' said Alice."
                       f"\n'Then it doesn't matter which way you go,' said the Cat."
                       f"\n'— so long as I get somewhere,' Alice added as an explanation."
                       f"\n'Oh, you're sure to do that,' said the Cat, 'if you only walk long enough.'")

# Виводимо змінну на друк
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азовське моря разом?
"""
s_black_sea = 436402 # задаємо площу Чорного моря
s_azov_sea = 37800 # задаємо площу Азовського моря
s_both_seas = s_black_sea + s_azov_sea # Обчислюємо площу обох морів разом

# Виводимо відповідь
print(f"Відповідь: {s_both_seas} км2 займають Чорне та Азовське моря разом.")


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
# Задаємо змінні відомих величин
storage_1_2_3 = 375291
storage_1_2 = 250449
storage_2_3 = 222950
storage_1 = storage_1_2_3 - storage_2_3 # Обчислюємо кількість товарів на першому складі
storage_3 = storage_1_2_3 - storage_1_2 # Обчислюємо кількість товарів на третьому складі
storage_2 = storage_1_2 - storage_1  # Обчислюємо кількість товарів на другому складі

print(f"Відповідь: На першому складі розміщено {storage_1} товарів, на другому - {storage_2} товарів, а на "
      f"третьому - {storage_3} товарів.")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, скориставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість компьютера.
"""
total_months = 18  # півтора року переводимо в кількість місяців - весь термін "Оплати частинами"
monthly_price = 1179  # грн треба платити в місяць
computer_price = monthly_price * total_months # Обчислюємо вартість компьютера

# Виводимо відповідь
print(f"Відповідь: {computer_price} - повна вартість компьютера.")

# task 07
"""
Знайди остачу від ділення чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
# Знаходимо остачу від ділення кожного числа
a = 8019%8
b = 9907%9
c = 2789%5
d = 7248%6
e = 7128%5
f = 19224%9
# Виводимо відповідь

print(f"Остача від ділення чисел: а - {a}, b - {b}, c - {c}, d - {d}, e - {e}, f - {f}")

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
# Обчислюємо вартість кожної позиції замовлення
pizza_big = 4*274
pizza_middle = 2*218
juice = 4*35
cake = 1*350
water = 3*21

# Обчислюємо повну вартість замовлення і виводимо відповідь
order = pizza_big + pizza_middle + juice + cake + water
print(f"Відповідь: Повна вартість замовлення {order} гривень.")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
all_pictures = 232
per_page = 8
# Обчислюємо кількість сторінок, чка знадобиться за умови, що фотографії або діляться порівну між сторінками, або ні
if all_pictures%per_page == 0:
    pages = all_pictures//per_page
else:
    pages = all_pictures//per_page + 1
# Виводимо відповідь
print (f"Відповідь: Ігорю знадобиться щонайменше {pages} сторінок")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на заправку під час цієї подорожі, 
кожного разу заправляючи пов-
ний бак?
"""
# Задаємо змінні відомих величин
distance = 1600  # відстань
fuel_per_100_km = 9  # літрів бензину на 100 км
tank_capacity = 48  # місткість бака в літрах

# Обчислюємо необхідну кількість бензину на всю подорож
total_fuel_needed = int((distance / 100) * fuel_per_100_km)

# Обчислюємо необхідну кількість повних баків(заїздів на заправку)
if total_fuel_needed % tank_capacity > 0:
    num_refuels = int((total_fuel_needed // tank_capacity) + 1)
else:
    num_refuels = int(total_fuel_needed // tank_capacity)

# Виводимо відповідь
print(f"Загальна кількість бензину, необхідного для подорожі: {total_fuel_needed} літрів.")
print(f"Щонайменше разів родині необхідно заїхати на заправку: {num_refuels}.")
