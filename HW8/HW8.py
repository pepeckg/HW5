import sqlite3

# conn = sqlite3.connect('company_database.db')
# cursor = conn.cursor()
#
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS countries (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         title TEXT NOT NULL
#     )
# ''')
#
# cursor.executemany('INSERT INTO countries (title) VALUES (?)', [('США',), ('Германия',), ('Китай',)])
#
#
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS cities (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         title TEXT NOT NULL,
#         area REAL DEFAULT 0,
#         country_id INTEGER,
#         FOREIGN KEY (country_id) REFERENCES countries(id)
#     )
# ''')
#
#
# cursor.executemany('INSERT INTO cities (title, area, country_id) VALUES (?, ?, ?)',
#                    [('Нью-Йорк', 468.9, 1), ('Берлин', 891.85, 2), ('Пекин', 16410.54, 3),
#                     ('Лос-Анджелес', 1302.6, 1), ('Мюнхен', 310.7, 2), ('Шанхай', 6340.5, 3), ('Чикаго', 606.1, 1)])
#
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS employees (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         first_name TEXT NOT NULL,
#         last_name TEXT NOT NULL,
#         city_id INTEGER,
#         FOREIGN KEY (city_id) REFERENCES cities(id)
#     )
# ''')
#
# cursor.executemany('INSERT INTO employees (first_name, last_name, city_id) VALUES (?, ?, ?)',
#                    [('Иван', 'Иванов', 1), ('Елена', 'Смирнова', 2), ('Алексей', 'Петров', 3),
#                     ('Светлана', 'Сидорова', 4), ('Дмитрий', 'Федоров', 5), ('Ольга', 'Михайлова', 6),
#                     ('Максим', 'Козлов', 6), ('Татьяна', 'Новикова', 1), ('Андрей', 'Кузнецов', 2),
#                     ('Мария', 'Волкова', 3), ('Сергей', 'Степанов', 4), ('Наталья', 'Николаева', 5),
#                     ('Павел', 'Орлов', 6), ('Евгения', 'Андреева', 6), ('Артем', 'Григорьев', 1)])
#
# conn.commit()
# conn.close()

conn = sqlite3.connect('company_database.db')
cursor = conn.cursor()

cursor.execute('SELECT id, title FROM cities')
cities = cursor.fetchall()

print(
    'Вы можете отобразить список сотрудников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:')
for city in cities:
    print(f'{city[0]}. {city[1]}')

while True:
    selected_city_id = int(input('Введите id города: '))

    if selected_city_id == 0:
        break
    if selected_city_id not in [city[0] for city in cities]:
        print('Ошибка: Город с указанным ID не найден.')
        continue

    cursor.execute('''
        SELECT e.first_name, e.last_name, c.title, co.title, c.area
        FROM employees AS e
        JOIN cities AS c ON e.city_id = c.id
        JOIN countries AS co ON c.country_id = co.id
        WHERE c.id = ?
    ''', (selected_city_id,))

    employees = cursor.fetchall()

    if not employees:
        print('В данном городе нет сотрудников.')
    else:
        print(f'Сотрудники, проживающие в выбранном городе:')
        for employee in employees:
            print(
                f'{employee[0]} {employee[1]}, {employee[3]},город {employee[2]} с площадью: {employee[4]}')

conn.close()
