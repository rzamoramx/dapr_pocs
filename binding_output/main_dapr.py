
import json
import time

from dapr.clients import DaprClient


def publisher():
    with DaprClient() as daprc:
        n = 0
        while True:
            n += 1
            req_data = {
                'id': n,
                'message': 'hello world from Dapr and Confluent'
            }

            print(f'Sending message id: {req_data["id"]}, message "{req_data["message"]}"', flush=True)

            # Create a typed message with content type and body
            resp = daprc.invoke_binding('myevent', 'create', json.dumps(req_data))
            print(f"Resp: {resp}")
            time.sleep(3)


if __name__ == '__main__':
    publisher()
