from flask import Flask, jsonify, request
import requests
import json
import time

app = Flask(__name__)

def fetch_top_gainers():
    current_timestamp = int(time.time() * 1000)
    url = f"https://nepalipaisa.com/api/GetTopMarketMovers?indicator=gainers&sectorCode=&_={current_timestamp}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        result_data = data.get('result', [])  # Extract only the 'result' part
        return result_data
    else:
        raise Exception(f"Error: {response.status_code}")

@app.route('/get_top_gainers')
def get_top_gainers():
    try:
        data = fetch_top_gainers()
        return json.dumps(data, indent=2)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
