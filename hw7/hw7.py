import sqlite3

def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

def insert_product(conn, product):
    sql = '''INSERT INTO products 
    (product_title, price, quantity)
    VALUES(?, ?, ?)
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def update_product_quantity(conn, product):
    sql = '''UPDATE products SET quantity = ? WHERE id = ?    
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def update_product_price(conn, product):
    sql = '''UPDATE products SET price = ? WHERE id = ?    
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def delete_product(conn, id):
    sql = '''DELETE FROM products WHERE id = ?    
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def select_all_products(conn):
    sql = '''SELECT * FROM products    
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)

        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)

def select_products_by_price_and_quantity(conn, price_limit, quantity_limit):
    sql = '''SELECT * FROM products WHERE price <= ? and quantity >= ?    
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (price_limit, quantity_limit))

        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)

def select_products_by_title(conn, keyword):
    sql = '''SELECT * FROM products WHERE product_title LIKE ?
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, ('%' + keyword + '%',))

        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)



connection = create_connection('hw.db')
sql_create_products_table = '''
    CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price FLOAT(10,2) NOT NULL DEFAULT 0.0,        
    quantity INTEGER NOT NULL DEFAULT 0
    )
'''


if connection is not None:
    print('Successfully connected!')
    # create_table(connection, sql_create_products_table)
    # insert_product(connection, ('Apples', 125.0, 200))
    # insert_product(connection, ('Bananas', 220.0, 300))
    # insert_product(connection, ('Oranges', 250.0, 150))
    # insert_product(connection, ('Carrots', 87.5, 250))
    # insert_product(connection, ('Potatoes', 87.2, 350))
    # insert_product(connection, ('Onions', 46.8, 400))
    # insert_product(connection, ('Tomatoes', 152.8, 180))
    # insert_product(connection, ('Cucumbers', 76.2, 220))
    # insert_product(connection, ('Lettuce', 61.0, 150))
    # insert_product(connection, ('Chicken', 200.0, 100))
    # insert_product(connection, ('Salmon', 120.0, 50))
    # insert_product(connection, ('Pasta', 90.0, 300))
    # insert_product(connection, ('Rice Brown', 160.0, 120))
    # insert_product(connection, ('Beans', 99.9, 180))
    # insert_product(connection, ('Olive Oil', 550.0, 90))
    #
    # update_product_quantity(connection, (400, 2))
    # update_product_price(connection, (190, 13))
    # delete_product(connection, 12)
    # select_all_products(connection)
    # select_products_by_price_and_quantity(connection, 100, 5)
    # select_products_by_title(connection, 'Oranges')
    # select_products_by_title(connection, 'Bananas')


    connection.close()