import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("pricepulse.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            price TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_product(title, price):
    conn = sqlite3.connect("pricepulse.db")
    c = conn.cursor()
    c.execute("INSERT INTO products (title, price, timestamp) VALUES (?, ?, ?)", 
              (title, price, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()