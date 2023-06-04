import requests
import threading
import time
from flask import Flask, request
app = Flask(__name__)
@app.route('/', methods=["GET"])
def post_data():
    with open('whazzup.txt', 'r') as f:
        r = f.read()
        return r
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)