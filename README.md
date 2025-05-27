# 🛍️ PricePulse – E-Commerce Price Tracker & Smart Comparator

**PricePulse** is a full-stack web application that tracks Amazon product prices, visualizes historical price trends, and sends smart email alerts when prices drop below a desired threshold, it combines intelligent automation with a modern, responsive UI.

---

## 🚀 Features

- 🔍 **Track Amazon Products**  
  Enter any Amazon product URL to fetch and display its name, current price, and image.

- 📈 **Price History Visualization**  
  View price trends over time via an interactive chart powered by Chart.js.

- 📬 **Price Drop Alerts**  
  Set a target price and get email alerts via SendGrid when the product’s price drops below that level.

- ⏰ **Automated Price Monitoring**  
  Prices are automatically scraped every 30 minutes using APScheduler.

- 📱 **Responsive UI**  
  Built with Tailwind CSS to ensure a smooth experience across all devices.

---

## 🧰 Tech Stack

**Backend:**  
- Flask  
- Playwright (for web scraping)  
- SQLite (for storing product and price data)  
- APScheduler (for task scheduling)  
- SendGrid (for email notifications)

**Frontend:**  
- React Tailwind CSS  

---

## ⚙️ How It Works

1. **User submits an Amazon product URL.**  
2. **Playwright** scrapes the current price, title, and image.  
3. Product details are stored in **SQLite**.  
4. Every 30 minutes, **APScheduler** re-scrapes the product price.  
5. If the price drops below the user-set threshold, **SendGrid** sends an alert email.  
6. **Chart.js** visualizes historical pricing data on the frontend.

---
