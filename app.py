from flask import Flask, request, jsonify
from flask_cors import CORS
from scraper import Scraper
from data_saver import save_to_json
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    try:
        queries = request.json.get('queries', [])
        print(f"Received queries: {queries}")  # Log received queries
        scraper = Scraper()
        output_dir = 'scraped_data'
        os.makedirs(output_dir, exist_ok=True)

        results = {}
        for query in queries:
            print(f"Scraping results for: {query}")
            products = scraper.scrape(query)
            output_file = os.path.join(output_dir, f"{query}.json")
            save_to_json(products, output_file)
            results[query] = products
            print(f"Saved results to {output_file}")

        return jsonify(results)
    except Exception as e:
        print(f"Error: {e}")  # Log the error
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
