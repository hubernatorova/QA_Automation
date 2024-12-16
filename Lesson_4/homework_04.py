import re

adventures_of_tom_sawyer ="""\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adventures_of_tom_sawyer у завданнях 1-3
# task 01 ==
""" Дані у строці adventures_of_tom_sawyer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

# Замінюємо перенесення на пробіли
adventures_of_tom_sawyer = adventures_of_tom_sawyer.replace("\n", " ")

# Виводимо новий текст
print(adventures_of_tom_sawyer)

# task 02 ==
""" Замініть .... на пробіл
"""

# Замінюємо крапки на пробіли
adventures_of_tom_sawyer = adventures_of_tom_sawyer.replace("....", " ")

# Виводимо новий текст
print(adventures_of_tom_sawyer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

# Видаляємо зайві пробіли
adventures_of_tom_sawyer = re.sub(r'\s+', " ", adventures_of_tom_sawyer)

# Виводимо новий текст
print(adventures_of_tom_sawyer)

# task 04
""" Виведіть, скільки разів у тексті зустрічається літера "h"
"""

# Обчислюємо кількість літер "h" в тексті
adventures_of_tom_sawyer_h = adventures_of_tom_sawyer.count("h")

# Виводимо результат
print(adventures_of_tom_sawyer_h)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

# Знаходимо в тексті всі слова, що починаються з великої літери
adventures_of_tom_sawyer_capitalized = re.findall(r'\b[A-Z][a-z]*\b', adventures_of_tom_sawyer)

# Також це завдання можна виконати іншим методом:
# words = adventures_of_tom_sawyer.split()
# adventures_of_tom_sawyer_capitalized = [word for word in words if word[0].isupper()]

# Підраховуємо кількість таких слів
count = len(adventures_of_tom_sawyer_capitalized)

# Виводимо результати
print(f"Слова, що починаються з великої літери: {adventures_of_tom_sawyer_capitalized}")
print(f"Кількість слів: {count}")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

# Знаходимо позицію, на якій слово зустрічається вперше
first_tom = adventures_of_tom_sawyer.find("Tom")

# Знаходимо позицію, на якій слово зустрічається вдруге
second_tom = adventures_of_tom_sawyer.find("Tom", first_tom + 1)

# Виводимо результат
print(f"Позиція, на якій слово зустрічається вдруге: {second_tom}")

# task 07
""" Розділіть змінну adventures_of_tom_sawyer по кінцю речення.
Збережіть результат у змінній adventures_of_tom_sawyer_sentences
"""
# Замінюємо всі символи кінця речень на крапку на випадок, якщо вони присутні
adventures_of_tom_sawyer = adventures_of_tom_sawyer.replace("!", ".").replace("?", ".")

# Розділяємо текст за допомогою методу split
adventures_of_tom_sawyer_sentences = adventures_of_tom_sawyer.split(". ")

# Також можна виконати розділення за допомогою регулярних виразів
# adventures_of_tom_sawyer_sentences = re.split(r'(?<=[.!?])\s+', adventures_of_tom_sawyer)

# Можна вивести всі речення, щоб запевнитись в правильності коду
print(adventures_of_tom_sawyer_sentences)

# task 08
""" Виведіть четверте речення з adventures_of_tom_sawyer_sentences.
Перетворіть рядок у нижній регістр.
"""
# Для наочності можна спочатку дізнатись загальну кількість речень(елементів списку)
print (len(adventures_of_tom_sawyer_sentences))

# Оскільки четверте речення матиме індекс 3, виводимо його і переводимо в нижній регістр
print(adventures_of_tom_sawyer_sentences[3].lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

# Перевіряємо, чи починається якесь речення з "By the time"
for sentence in adventures_of_tom_sawyer_sentences:
    if sentence.startswith("By the time"):
        print(f"Речення, що починається з 'By the time': {sentence}")

# task 10
""" Виведіть кількість слів останнього речення з adventures_of_tom_sawyer_sentences.
"""

# Розділяємо останнє речення на слова та рахуємо їх кількість
word_count = len(adventures_of_tom_sawyer_sentences[-1].split())

# Виводимо кількість слів
print(f"Кількість слів в останньому реченні: {word_count}")