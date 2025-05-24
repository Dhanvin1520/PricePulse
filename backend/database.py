import sqlite3

def create_table():
    conn = sqlite3.connect('pricepulse.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT,
            title TEXT,
            price TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_price_data(url, title, price, timestamp):
    conn = sqlite3.connect('pricepulse.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO products (url, title, price, timestamp) VALUES (?, ?, ?, ?)',
                   (url, title, price, timestamp))
    conn.commit()
    conn.close()

def get_all_prices():
    conn = sqlite3.connect('pricepulse.db')
    cursor = conn.cursor()
    cursor.execute('SELECT title, price, timestamp FROM products ORDER BY timestamp DESC')
    rows = cursor.fetchall()
    conn.close()

    return [
        {"title": row[0], "price": row[1], "timestamp": row[2]}
        for row in rows
    ]