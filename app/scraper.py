import requests
from bs4 import BeautifulSoup
import re
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv
import os

load_dotenv()

def scrape_amazon(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract product name
        name = soup.find('span', id='productTitle')
        name = name.text.strip() if name else "Unknown Product"
        
        # Extract price
        price = soup.find('span', class_='a-price-whole')
        price = float(re.sub(r'[^\d.]', '', price.text)) if price else 0.0
        
        # Extract image
        image = soup.find('img', id='landingImage')
        image_url = image['src'] if image else ""
        
        return {'name': name, 'price': price, 'image_url': image_url}
    except Exception as e:
        print(f"Error scraping Amazon: {e}")
        return None

def send_price_alert(email, product_name, current_price, target_price, product_url):
    message = Mail(
        from_email='your-email@example.com',  # Replace with your verified SendGrid sender
        to_emails=email,
        subject=f'Price Drop Alert: {product_name}',
        html_content=f"""
        <h3>Price Drop Alert!</h3>
        <p>Product: {product_name}</p>
        <p>Current Price: ₹{current_price}</p>
        <p>Target Price: ₹{target_price}</p>
        <p><a href="{product_url}">View Product</a></p>
        """
    )
    try:
        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
        sg.send(message)
        print(f"Email sent to {email}")
    except Exception as e:
        print(f"Error sending email: {e}")