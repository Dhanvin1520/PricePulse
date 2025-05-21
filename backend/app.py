from flask import Flask, request, jsonify
from scraper import scrape_price

app = Flask(__name__)

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    price = scrape_price(url)
    return jsonify({'price': price})

if __name__ == '__main__':
    app.run(debug=True)