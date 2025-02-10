"""
Генератори:
Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.

Ітератори:
Реалізуйте ітератор для зворотного виведення елементів списку.
Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.

Декоратори:
Напишіть декоратор, який логує аргументи та результати викликаної функції.
Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
"""
from collections.abc import Iterator


def even_numbers(N):
    """Генератор парних чисел від 0 до N."""
    for num in range(0, N + 1, 2):
        yield num

def fibonacci(N):
    """Генератор чисел Фібоначчі до N."""
    a, b = 0, 1
    while a <= N:
        yield a
        a, b = b, a + b


class ReverseListIterator(Iterator):
    """Ітератор для зворотного виведення елементів списку."""

    def __init__(self, lst):
        self.lst = lst
        self.index = len(lst) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.lst[self.index]
        self.index -= 1
        return value


class EvenNumbersIterator(Iterator):
    """Ітератор, який повертає всі парні числа в діапазоні від 0 до N."""

    def __init__(self, N):
        self.N = N
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.N:
            raise StopIteration
        result = self.current
        self.current += 2
        return result


def log_function(func):
    """Декоратор, який логує аргументи та результат виклику функції."""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Виклик {func.__name__} з аргументами {args}, {kwargs} -> Результат: {result}")
        return result
    return wrapper

def exception_handler(func):
    """Декоратор, який перехоплює та обробляє винятки, що виникають у функції."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Помилка у {func.__name__}: {e}")
    return wrapper
