
import json
from dapr.ext.grpc import App, BindingRequest

app = App()


@app.binding('myevent')
def binding(request: BindingRequest):
    data = json.loads(request.text())
    print(f'Received: id={data["id"]}, message="{data["message"]}"', flush=True)
    # print(request.text(), flush=True)


if __name__ == '__main__':
    app.run(3000)
