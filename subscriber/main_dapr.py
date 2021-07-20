
#from flask_cors import CORS
from cloudevents.sdk.event import v1
from dapr.ext.grpc import App
import json

app = App()
#CORS(app)


@app.subscribe(pubsub_name='pubsub', topic='B')
def topic_a(event: v1.Event) -> None:
    data = json.loads(event.Data())
    print(f'Received: id={data["id"]}, message="{data ["message"]}"'
          ' content_type="{event.content_type}"', flush=True)


if __name__ == '__main__':
    app.run(3000)
