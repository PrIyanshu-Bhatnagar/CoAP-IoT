from coapthon.client.helperclient import HelperClient

client = None
path = "basic"


def client_1_connect():
    global client

    host = "127.0.0.1"
    port = 5683
    client = HelperClient(server=(host, port)) #Connection to server


def client_1_stop():
    client.stop()

def client_1_get():
    response = client.get(path=path)
    print response.pretty_print()

def client_1_post(payload):
    response = client.put(path=path, payload=payload)
    print response.pretty_print()

def client_1_put(payload):
    response = client.put(path=path, payload=payload)
    print response.pretty_print()
