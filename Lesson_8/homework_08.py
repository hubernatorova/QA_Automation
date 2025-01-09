# Створіть масив зі строками, які будуть складатися з чисел, які розділені комою. Наприклад:
# [”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]
# Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).
# Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі), вам потрібно зловити вийняток і вивести “Не можу це зробити!”
# Використовуйте блок try\except, щоб уникнути інших символів, окрім чисел у списку.
# Для цього прикладу правильний вивід буде - 10, 60, “Не можу це зробити”

"""Варіант 1"""
def calculate_sum(string):
    try:
        numbers = string.split(",") # Розділяємо строку за комами
        numbers = [int(num) for num in numbers] # Перетворюємо кожен елемент у число
        return sum(numbers) # Повертаємо суму чисел
    except ValueError:
        return "Не можу це зробити!" # У разі помилки перетворення виводимо повідомлення
# Оголошуємо список строк
string_list = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]
# Проходимо по кожній строці і виводимо результат
for string in string_list:
    print(calculate_sum(string))

"""Варіант 2 - той, що ми розглядали на занятті"""
lst_homework = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

def homework(lst):
    result = []
    for val in lst:
        lst1 = val.split(",")
        try:
            lst2 = [int(i) for i in lst1]
            res = sum(lst2)
            result.append(res)
        except ValueError:
            res = "Не можу це зробити!"
            result.append(res)
    return result
print(homework(lst_homework))