import json

from dapr.clients import DaprClient

from dapr.ext.grpc import App, InvokeMethodRequest, InvokeMethodResponse

STORE_NAME = 'statestoref'
app = App()


@app.method(name='neworder')
def new_order(request: InvokeMethodRequest) -> InvokeMethodResponse:
    print("*********INCOMING REQUEST**********")
    print(request.metadata, flush=True)
    print(request.text(), flush=True)

    data = json.loads(request.text())
    save_state(f'order{data["id"]}', data["message"])
    return InvokeMethodResponse(b'INVOKE_RECEIVED', "text/plain; charset=UTF-8")


def save_state(key, value):
    with DaprClient() as daprc:
        daprc.save_state(store_name=STORE_NAME, key=key, value=value)
        print(f"State store has successfully saved {value} with {key} as key")


app.run(3000)
