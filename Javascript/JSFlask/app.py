import requests
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/convert', methods=["POST"])
def convert():
    currency = request.form.get("currency")
    res = requests.get("http://api.exchangeratesapi.io/v1/latest", params={
        "access_key": "3ea1207d566f803ad05160439d06c2c1",
        #"base": "USD",
        "symbols": currency
    })

    if res.status_code != 200:
        return jsonify({"success": False, "response": res.json()})

    data = res.json()
    if currency not in data.get("rates", {}):
        return jsonify({"success": False})

    return jsonify({"success": True, "rate": data["rates"][currency]})

if __name__ == '__main__':
    app.run(debug=True)
