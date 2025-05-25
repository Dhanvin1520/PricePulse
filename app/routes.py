from flask import Blueprint, request, render_template, jsonify
from app.scraper import scrape_amazon
from app.database import add_product, add_price, get_product, get_prices, add_alert

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/track', methods=['POST'])
def track():
    url = request.form['url']
    email = request.form.get('email', '')
    target_price = float(request.form.get('target_price', 0))
    
    data = scrape_amazon(url)
    if not data:
        return jsonify({'error': 'Failed to scrape product'}), 400
    
    product_id = add_product(url, data['name'], data['image_url'])
    add_price(product_id, data['price'])
    
    if email and target_price:
        add_alert(product_id, email, target_price)
    
    return jsonify({
        'product_id': product_id,
        'name': data['name'],
        'image_url': data['image_url'],
        'current_price': data['price']
    })

@bp.route('/product/<int:product_id>')
def get_product_data(product_id):
    product = get_product(product_id)
    prices = get_prices(product_id)
    return jsonify({
        'product': {'id': product[0], 'name': product[2], 'image_url': product[3], 'url': product[1]},
        'prices': [{'price': p[0], 'timestamp': p[1]} for p in prices]
    })