from apscheduler.schedulers.background import BackgroundScheduler
from scraper import scrape_amazon_product
from database import insert_price_data
from datetime import datetime


urls_to_scrape = [
    "https://www.amazon.in/dp/B0CHD2G6M8",
]

def scrape_and_store():
    for url in urls_to_scrape:
        data = scrape_amazon_product(url)
        print(f"[{datetime.now()}] Scraped: {data}")
        insert_price_data(url, data["title"], data["price"], datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scrape_and_store, 'interval', hours=1)
    scheduler.start()