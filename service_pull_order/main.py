
import os
import time
import requests

DAPR_PORT = os.getenv("DAPR_HTTP_PORT", 3500)
DAPR_URL = "http://localhost:{}/v1.0/invoke/serviceorder/method/neworder".format(DAPR_PORT)


def main():
    n = 0
    while True:
        n += 1
        message = {"data": {"order_id": n}}

        try:
            response = requests.post(DAPR_URL, json=message)
            print(f"RESPONSE: {response}")
        except Exception as e:
            print(e)

        time.sleep(2)


if __name__ == '__main__':
    main()
