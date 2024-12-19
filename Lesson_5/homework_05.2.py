# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

# створюємо копію списку для проведення маніпуляцій з ним
people_records_copy = people_records.copy()

# Додаємо новий запис на початок списку
people_records_copy.insert(0, ('Nataliia', 'Hubernatorova', 40,'QA', 'Kyiv'))

# міняємо місцями елементи з індексами 1 і 5
people_records_copy[1], people_records_copy[5] = people_records_copy[5], people_records_copy[1]

# визначаємо необхідні індекси для перевірки віку
check_age_indexes = [6, 10, 13]

# оголошуємо порожній список куди додамо людей, які не відповідають умові віку >=30
younger_people = []

# перевіряємо умову, розпаковуючи дані кожної людини під необхідним індексом
for index in check_age_indexes:
    first_name, last_name, age, profession, city = people_records_copy[index]
    if age < 30:
      # додаємо в список імʼя, прізвище та вік людей, які не відповідають умові
        younger_people.append((first_name, last_name, age))

# прописуємо умову виводу результата
if not younger_people:
    print("All people in modified list with records indexes 6, 10, 13 have age >= 30")
else:
    print("There are some people here who are younger than 30:")
    # проходимся циклом по списку молодших людей і виводимо імʼя, прізвище та вік цих людей
    for first_name, last_name, age in younger_people:
        print(f"{first_name} {last_name}, Age: {age}")



