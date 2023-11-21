from flask import Flask, request, render_template
from pymongo import MongoClient
import time
from datetime import datetime


app = Flask(__name__)

# MongoDBクライアントの設定
client = MongoClient('127.0.0.1', 27017)
db = client['ESP32']
collection = db['accl']

@app.route('/data', methods=['POST'])
def data():
    data = request.json
    timestamp = data['timestamp']
    datetime_obj = datetime.utcfromtimestamp(timestamp / 1000.0)
    data['timestamp'] = datetime_obj
    collection.insert_one(data)  # データをMongoDBに挿入
    return 'Data received'

@app.route('/data')
def view_data():
    data = list(collection.find())
    return render_template('data.html', data=data)

@app.route('/')
def index():
    while True:
        # MongoDBからデータを取得
        data = list(collection.find())

        # 取得したデータをJSON形式に変換
        data_json = [{'label': item['timestamp'], 'value': item['acceleration_x']} for item in data]

        return render_template('index.html', data_json=data_json)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
