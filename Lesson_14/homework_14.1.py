class Student:
    def __init__(self, firstname, lastname, age, average_grade):
        """Метод ініціалізує обʼєкт 'студент', куди передаються наступні параметри:
        імʼя, прізвище, вік та середній бал"""
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.average_grade = average_grade

    def upgrade_average_grade(self, new_average_grade):
        """Метод оновлює середній бал"""
        self.average_grade = new_average_grade

    def __str__(self):
        """Метод повертає інформацію про студента в читабельному вигляді"""
        return (f"Student: {self.firstname} {self.lastname}, Age: {self.age}, "
                f"Average Grade: {self.average_grade}")


# Створення об'єкта класу "Студент"
student = Student("Наталія", "Губернаторова", 40, 91)

# Виведення інформації про студента
print(student)

# Зміна середнього балу студента
student.upgrade_average_grade(100)

# Виведення оновленої інформації про студента
print(student)