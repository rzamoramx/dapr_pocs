

import json
import time

from dapr.clients import DaprClient

with DaprClient() as daprc:
    count = 1

    req_data = {
        'id': count,
        'message': 'hello world from Dapr'
    }

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
