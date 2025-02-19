import sqlite3
import pandas as pd

# Створюємо підключення до тимчасової бази даних, якщо треба постійна БД, то використовуємо conn = sqlite3.connect("shop.db")
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# Створюємо таблицю категорій
cursor.execute( # language=SQL
     '''
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    )
''')

# Створюємо таблицю продуктів
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        price REAL NOT NULL,
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES categories (id) ON DELETE SET NULL
    )
''')

# Додаємо категорії товарів
cursor.executemany("""
INSERT INTO categories (name) VALUES (?)
""", [
    ('Смартфони',),
    ('Ноутбуки',),
    ('Аксесуари',),
])

# Додаємо дані в таблицю продуктів
cursor.executemany('''
    INSERT INTO products (name, description, price, category_id) 
    VALUES (?, ?, ?, ?)
''', [
    ('iPhone 15', 'Смартфон Apple', 999.99, 1),
    ('Samsung Galaxy S23', 'Флагманський смартфон Samsung', 899.99, 1),
    ('MacBook Pro 16', 'Ноутбук Apple', 2499.99, 2),
    ('ASUS ROG Strix', 'Ігровий ноутбук', 1799.99, 2),
    ('Чохол для iPhone', 'Силіконовий чохол', 19.99, 3)
])

# Зберігаємо зміни
conn.commit()

# Створюємо функцію, яка буде створювати SQL запити і виводити результати через pandas.DataFrame

def run_query(query):
    df = pd.read_sql_query(query, conn)
    print(df)

# Виконуємо різні види JOIN запитів
run_query('''
    SELECT products.id, products.name, products.description, products.price, categories.name AS category
    FROM products
    INNER JOIN categories ON products.category_id = categories.id
''')

run_query('''
    SELECT products.id, products.name, products.description, products.price, categories.name AS category
    FROM products
    LEFT JOIN categories ON products.category_id = categories.id
''')

# Оскільки в sqLite немає RIGHT JOIN, то робимо обернений LEFT JOIN
run_query('''
    SELECT categories.id, categories.name AS category, products.name AS product, products.price
    FROM categories
    LEFT JOIN products ON categories.id = products.category_id
''')

run_query('''
    SELECT products.id, products.name, products.description, products.price, categories.name AS category
    FROM products
    LEFT JOIN categories ON products.category_id = categories.id
    UNION
    SELECT products.id, products.name, products.description, products.price, categories.name AS category
    FROM products
    RIGHT JOIN categories ON products.category_id = categories.id
''')


# Закриваємо підключення
conn.close()