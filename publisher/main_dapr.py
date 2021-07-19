
import json
import time

from dapr.clients import DaprClient

with DaprClient() as daprc:
    msg_id = 0
    while True:
        msg_id += 1
        req_data = {
            'id': msg_id,
            'message': 'Hola pubsub usando grpc'
        }

        # Create a typed message with content type and body
        resp = daprc.publish_event(
            pubsub_name='pubsub',
            topic_name='A',
            data=json.dumps(req_data),
            data_content_type='application/json',
        )

        # Print the request
        print(req_data, flush=True)
        time.sleep(4)
