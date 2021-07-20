

import json
import time

from dapr.clients import DaprClient

with DaprClient() as daprc:
    req_data = {
        'id': 1,
        'message': 'hello world from Dapr'
    }

    count = 1
    while True:
        resp = daprc.invoke_method(
            'serviceorder',
            'neworder',
            data=json.dumps(req_data),
        )

        print(resp.content_type, flush=True)
        print(resp.text(), flush=True)

        time.sleep(3)

        count += 1
        req_data["id"] = count
