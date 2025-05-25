from apscheduler.schedulers.background import BackgroundScheduler
from app.scraper import scrape_amazon, send_price_alert
from app.database import get_product, add_price, get_alerts, update_alert_status

def schedule_scraping():
    scheduler = BackgroundScheduler()
    
    def job():
        conn = sqlite3.connect('prices.db')
        c = conn.cursor()
        c.execute("SELECT id, url FROM products")
        products = c.fetchall()
        conn.close()
        
        for product_id, url in products:
            data = scrape_amazon(url)
            if data and data['price']:
                add_price(product_id, data['price'])
                alerts = get_alerts(product_id)
                product = get_product(product_id)
                for alert in alerts:
                    email, target_price, alerted = alert
                    if data['price'] <= target_price and not alerted:
                        send_price_alert(email, product[2], data['price'], target_price, url)
                        update_alert_status(alert[0])
    
    scheduler.add_job(job, 'interval', minutes=30)
    scheduler.start()