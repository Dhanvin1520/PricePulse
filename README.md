#Day 6 
not able to commit the updated file due to error in commit .env file
# PricePulse - E-Commerce Price Tracker & Smart Comparator
PricePulse is a full-stack web application that enables users to track prices of Amazon products, visualize price trends over time, and receive email alerts when prices drop below a specified threshold. Additionally, it offers an optional AI-powered feature to compare prices across platforms like Flipkart and Meesho.


## Features

- **Input Amazon URL**: Users can enter an Amazon product URL to start tracking.
- **Price Tracking**: Automatically scrapes and records the product’s price every 30 minutes.
- **Price Trend Visualization**: Displays a line graph of historical prices using Chart.js.
- **Product Details**: Shows product name, image, and current price.
- **Price Drop Alerts**: Sends email notifications via SendGrid when the price falls below a user-defined threshold.
  

---

## Tech Stack

- **Frontend**: React, Chart.js, Axios
- **Backend**: Flask, BeautifulSoup (for scraping), APScheduler (for scheduling), SendGrid (for emails), Flask-CORS
- **Database**: SQLite (local) or PostgreSQL (production on Render)
- **Deployment**: Vercel (frontend), Render (backend)
- : Gemini API for cross-platform price comparison
