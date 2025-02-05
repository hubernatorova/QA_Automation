import randominfo
person = randominfo.Person()
print(person.full_name, person.gender, person.hobbies, person.address, person.country)

"""
Для того, щоб позбутись помилки я модифікувала методи класа Person: 
- метод get_country повертав хоббі замість країни, тепер повертає помилку? оскільки в файлі немає колонки country,
- метод get_hobbies повертав дані за неправильним індексом, додала його в прінт
- метод get_address повертав невірні дані( не за тими індексами), а також звертався до порожнього списку і через це 
поверталась помилка IndexError: Cannot choose from an empty sequence
Наразі модуль працює корректно для цих 5 методів
"""
