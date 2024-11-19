from flask import Flask, request, jsonify
import requests
from flask_cors import CORS  # הוספת CORS

app = Flask(__name__)
CORS(app)  # מאפשר CORS לכל הבקשות

def convert_to_hebrew_date(iso_date):
    url = "https://www.hebcal.com/converter"
    params = {
        "cfg": "json",
        "gy": iso_date.split("-")[0],
        "gm": iso_date.split("-")[1],
        "gd": iso_date.split("-")[2],
        "g2h": 1
    }

    # הדפסת הפרמטרים שנשלחים ל-API
    print(f"Sending request to Hebcal with URL: {url}")
    print(f"Params: {params}")

    response = requests.get(url, params=params)

    # הדפסת הסטטוס והתגובה מה-API
    print(f"API Response Status Code: {response.status_code}")
    print(f"API Response Text: {response.text}")

    if response.status_code == 200:
        return response.json()

    return {"error": "Failed to fetch data"}

@app.route('/convert', methods=['POST'])
def convert():
    data = request.json
    iso_date = data.get('date')
    if not iso_date:
        return jsonify({"error": "Date is required"}), 400

    hebrew_date = convert_to_hebrew_date(iso_date)
    return jsonify(hebrew_date)

if __name__ == '__main__':
    app.run(debug=True)
