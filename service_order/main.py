import json
import os
from flask import Flask, request
import requests


DAPRPORT = os.getenv("DAPR_HTTP_PORT", 3500)
STATESTORENAME = 'statestore'
STATEURL = f'http://localhost:{DAPRPORT}/v1.0/state/{STATESTORENAME}'
app = Flask(__name__)


@app.route('/health', methods=["GET"])
def health():
    return "OK", 200


@app.route('/neworder', methods=['POST'])
def new_order():
    print(f'request: {request.json}')
    orderId = request.json["data"]['order_id']
    print(f'Gor a new order, ID: {orderId}')

    state = [{
        "key": "order",
        "value": request.json['data']
    }]

    print(f'DDDDDDD: {json.dumps(state)}')  #

    response = requests.post(STATEURL, data=json.dumps(state))
    print(f'XXXXXX {response.status_code}')
    if response.status_code == 200 or response.status_code == 204:
        return {"status": "ok"}, 200
    else:
        print(f'[ERROR] on persist key to store: {response.content}')
        return {"status": "nok"}, 500


@app.route('/order', methods=['GET'])
def get_order():
    #print(f'request: {request.json}')
    # Get last entry of "order" key from redis store
    response = requests.get(f"{STATEURL}/order")
    print(f'XXXXXX {response.status_code}')
    if response.status_code == 200 or response.status_code == 204:
        return {"value": response.text}, 200
    else:
        print(f'[ERROR] on getting key from store: {response.content}')
        return {"status": "nok"}, 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3001)
