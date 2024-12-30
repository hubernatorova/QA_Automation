# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та виправити\доповнити.
"""


def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 10:
        result = number * multiplier
        if result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""


def summa(num_1, num_2):
    return num_1 + num_2


"""Далі викликаємо функцію і передаєм до неї на вхід необхідні значення"""
# наприклад:
print(summa(98, 109))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


def average(*args):
    """Приймає елементи списку як позиційні аргументи. Не списком. Наприклад average(1,2,3,4)"""
    return sum(args) / len(args)


print(average(86, 98, 138, 48958, 5, 78, 1, 2))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def palindrome(string):
    return string[::-1]

print(palindrome("hello"))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def most_long_word(*words_list):
    """Приймає елементи списку як позиційні аргументи. Не списком. Наприклад words_list("1", "f2", "hdw3")"""
    result = sorted(words_list, key=len)[-1]
    return result

print(most_long_word("hello", "worlds", "palindrom", "dfgwkrq2uro3ri"))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str_1, str_2):
    return str_1.find(str_2)


str_1 = "Hello, world!"
str_2 = "world"
print(find_substring(str_1, str_2))  # поверне 7

str_1 = "The quick brown fox jumps over the lazy dog"
str_2 = "cat"
print(find_substring(str_1, str_2))  # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обов'язково документуйте функції та дайте зрозумілі імена змінним.
"""
# task 7
""" Виведіть, скільки разів у тексті зустрічається літера "h"
"""
def h_count(some_text):
    """Функція на вхід приймає текст і підраховує в ньому всі літери 'h' """
    return some_text.count("h")

some_text = ('Tom gave up the brush with reluctance in his face but alacrity in his heart. '
        'And while the late steamer "Big Missouri" worked and sweated in the sun, '
        'the retired artist sat on a barrel in the shade close by, dangled his legs, '
        'munched his apple, and planned the slaughter of more innocents. '
        'There was no lack of material; boys happened along every little while; they came to jeer, '
        'but remained to whitewash. By the time Ben was fagged out, '
        'Tom had traded the next chance to Billy Fisher for a kite, in good repair; '
        'and when he played out, Johnny Miller bought in for a dead rat and a string to swing it with—and so on, '
        'and so on, hour after hour. And when the middle of the afternoon came, from being a poor poverty, '
        'stricken boy in the morning, Tom was literally rolling in wealth.')
print(h_count(some_text))

# task 8
"""Пишемо функцію, яка відсортує машини за ціною"""

def sort_cars_by_price(car_data):
    """Сортуємо словник за ціною (пʼятий елемент кортежа) і виводимо результат у вигляді словника"""
    return sorted(car_data.items(), key=lambda x: x[1][4])

car_data = {
  'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
  'Audi': ('black', 2020, 2.0, 'sedan', 55000),
  'BMW': ('white', 2018, 3.0, 'suv', 70000),
  'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
  'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
  'Honda': ('red', 2017, 1.5, 'sedan', 30000),
  'Ford': ('green', 2019, 2.3, 'suv', 40000),}

print (dict(sort_cars_by_price(car_data)))

# task 9
"""Пишемо функцію, яка підраховує кількість унікальних символів в строці.
Якщо їх понад 10 - виводе в консоль True, інакше - False."""

def count_unique_symbols(string_text):
    """Функція приймає на вхід текст, елементи перетворює на сет, та підраховує довжину сета.
    За умовою, якщо кількість елементів сета більше чи менш як 10, виводить відповідний результат """
    unique_symbols = len(set(string_text))
    if unique_symbols > 10:
        return True
    else:
        return False

string_text = "абабагаламага"
print(count_unique_symbols(string_text))

# task 10
"""Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера 'h'
(враховуються як великі, так і маленькі).
Цикл не повинен завершитися, якщо користувач ввів слово без букви 'h'"""

def input_h_cycle():
    """Функція вимагає від користувача ввести слово, яке містить букву 'h' або 'H'."""
    while True:
        word = input("Введіть слово, в якому є літера 'h' або 'H': ")
        if 'h' in word.lower():  # Перевіряємо наявність 'h' (незалежно від регістру)
            print("Дякую! Ви ввели слово:", word)
            break
        else:
            print("Це слово не містить літери 'h'. Спробуйте ще раз.")

    # Виклик функції

input_h_cycle()