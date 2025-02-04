"""Завдання 1
Створіть клас Employee, який має атрибути name та salary. Далі створіть два класи, Manager та Developer, які
успадковуються від Employee. Клас Manager повинен мати додатковий атрибут department, а клас Developer -
атрибут programming_language.
Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer. Цей клас представляє керівника
з команди розробників. Клас TeamLead повинен мати всі атрибути як Manager (ім'я, зарплата, відділ), а також атрибут
team_size, який вказує на кількість розробників у команді, якою керує керівник.
Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead

Завдання 2
Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру. Наслідуйте від нього
декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру. Властивості по типу
“довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор. Створіть Декілька різних
об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної."""

from abc import ABC, abstractmethod

# Завдання 1
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)  # Явный вызов конструктора Employee
        self.department = department


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)  # Явный вызов конструктора Employee
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        # Явный вызов конструктора Manager и Developer
        Manager.__init__(self, name, salary, department)  # Инициализация Manager
        Developer.__init__(self, name, salary, programming_language)  # Инициализация Developer
        self.team_size = team_size  # Атрибут TeamLead


# Тест на наявність атрибутів у TeamLead
team_lead = TeamLead("Alex", 100000, "Development", "Python", 5)
assert hasattr(team_lead, 'name')
assert hasattr(team_lead, 'salary')
assert hasattr(team_lead, 'department')
assert hasattr(team_lead, 'programming_language')
assert hasattr(team_lead, 'team_size')
print("Test passed: All required attributes exist in TeamLead")



# Завдання 2
class Figure(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass


class Rectangle(Figure):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_area(self):
        return self.__width * self.__height

    def get_perimeter(self):
        return 2 * (self.__width + self.__height)


class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def get_area(self):
        return 3.14159 * self.__radius ** 2

    def get_perimeter(self):
        return 2 * 3.14159 * self.__radius


# Створення об'єктів фігур
shapes = [
    Rectangle(4, 5),
    Circle(3),
    Rectangle(7, 2)
]

# Обчислення та виведення площі та периметру
for shape in shapes:
    print(f"{shape.__class__.__name__}: Area = {shape.get_area()}, Perimeter = {shape.get_perimeter()}")
