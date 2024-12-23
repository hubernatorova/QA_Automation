# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h"
# (враховуються як великі, так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

# Оголошуємо порожній рядок, куди будемо зберігати введене користувачем слово
users_input_word = ""

# Прописуємо цикл, який буде продовжуватись, доки слово не містить літери 'h' або 'H'
while 'h' not in users_input_word.lower():
    users_input_word = input("Введіть слово, яке містить літеру 'h': ")
    if 'h' not in users_input_word.lower():
        print("Спробуйте ще раз! У слові немає літери 'h'.")

print("Ви успішно ввели потрібне слово.")

# Також можна створити ще такий цикл:
# while True:
#     users_input_word = input("Введіть слово, яке містить літеру 'h': ")
#     if 'h' in users_input_word.lower():
#         print("Ви успішно ввели потрібне слово.")
#         break  # Виходимо з цикла, якщо умова виконана
#     else:
#         print("Спобуйте ще раз! У слові немає літери 'h'.")