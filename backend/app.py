from flask import Flask, render_template, request, jsonify
from database import create_table, insert_price_data, get_all_prices
from scraper import scrape_amazon_product
from scheduler import start_scheduler
from datetime import datetime

app = Flask(__name__)
create_table()
start_scheduler()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit-url', methods=['POST'])
def submit_url():
    try:
        url = request.form['url']
        data = scrape_amazon_product(url)  

        insert_price_data(url, data['title'], data['price'], datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        return jsonify(data)
    except Exception as e:
   
        print(f"Error in /submit-url: {e}")

        return jsonify({'error': str(e)}), 500
@app.route('/history')
def history():
    records = get_all_prices()
    return jsonify(records)

if __name__ == '__main__':
    app.run(debug=True)