from flask import Flask, jsonify, request
import requests
import json
import time

app = Flask(__name__)

def fetch_top_gainers(limit):
    current_timestamp = int(time.time() * 1000)
    url = f"https://nepalipaisa.com/api/GetTopMarketMovers?indicator=gainers&sectorCode=&limit={limit}&_={current_timestamp}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        result_data = data.get('result', [])  # Extract only the 'result' part
        return result_data
    else:
        raise Exception(f"Error: {response.status_code}")

@app.route('/get_top_gainers')
def get_top_gainers_route():
    try:
        # Retrieve limit parameter from the request URL, default to 25 if not provided
        limit = request.args.get('limit', default=25, type=int)
        data = fetch_top_gainers(limit)
        return json.dumps(data, indent=2)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
