import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('prices.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT NOT NULL,
        name TEXT,
        image_url TEXT
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS prices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER,
        price REAL,
        timestamp TEXT,
        FOREIGN KEY (product_id) REFERENCES products(id)
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS alerts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER,
        email TEXT,
        target_price REAL,
        alerted INTEGER DEFAULT 0,
        FOREIGN KEY (product_id) REFERENCES products(id)
    )''')
    conn.commit()
    conn.close()

def add_product(url, name, image_url):
    conn = sqlite3.connect('prices.db')
    c = conn.cursor()
    c.execute("INSERT INTO products (url, name, image_url) VALUES (?, ?, ?)", 
              (url, name, image_url))
    product_id = c.lastrowid
    conn.commit()
    conn.close()
    return product_id

def add_price(product_id, price):
    conn = sqlite3.connect('prices.db')
    c = conn.cursor()
    c.execute("INSERT INTO prices (product_id, price, timestamp) VALUES (?, ?, ?)",
              (product_id, price, datetime.now().isoformat()))
    conn.commit()
    conn.close()

def get_product(product_id):
    conn = sqlite3.connect('prices.db')
    c = conn.cursor()
    c.execute("SELECT * FROM products WHERE id = ?", (product_id,))
    product = c.fetchone()
    conn.close()
    return product

def get_prices(product_id):
    conn = sqlite3.connect('prices.db')
    c = conn.cursor()
    c.execute("SELECT price, timestamp FROM prices WHERE product_id = ? ORDER BY timestamp", 
              (product_id,))
    prices = c.fetchall()
    conn.close()
    return prices

def add_alert(product_id, email, target_price):
    conn = sqlite3.connect('prices.db')
    c = conn.cursor()
    c.execute("INSERT INTO alerts (product_id, email, target_price) VALUES (?, ?, ?)",
              (product_id, email, target_price))
    conn.commit()
    conn.close()

def get_alerts(product_id):
    conn = sqlite3.connect('prices.db')
    c = conn.cursor()
    c.execute("SELECT email, target_price, alerted FROM alerts WHERE product_id = ?", 
              (product_id,))
    alerts = c.fetchall()
    conn.close()
    return alerts

def update_alert_status(alert_id):
    conn = sqlite3.connect('prices.db')
    c = conn.cursor()
    c.execute("UPDATE alerts SET alerted = 1 WHERE id = ?", (alert_id,))
    conn.commit()
    conn.close()