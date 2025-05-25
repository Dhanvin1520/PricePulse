from flask import Flask, render_template, request, jsonify
from scraper import scrape_amazon_product
from database import add_price, get_price_history, add_alert

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/track', methods=['POST'])
def track_price():
    url = request.form.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    product_name, price = scrape_amazon_product(url)
    if product_name and price:
        add_price(url, product_name, price)
        return jsonify({'product_name': product_name, 'current_price': price})
    return jsonify({'error': 'Failed to scrape product'}), 500

@app.route('/history/<path:product_url>')
def price_history(product_url):
    history = get_price_history(product_url)
    return jsonify(history)

@app.route('/set_alert', methods=['POST'])
def set_alert():
    url = request.form.get('url')
    email = request.form.get('email')
    target_price = float(request.form.get('target_price'))
    if not url or not email or not target_price:
        return jsonify({'error': 'All fields are required'}), 400

    add_alert(url, email, target_price)
    return jsonify({'message': 'Alert scheduled'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)