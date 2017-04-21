from coapthon.client.helperclient import HelperClient

client = None
path = "basic"


def client_2_connect():
    global client

    host = "127.0.0.1"
    port = 5683
    client = HelperClient(server=(host, port)) #Connection to server


def client_2_stop():
    client.stop()

def client_2_get():
    response = client.get(path=path)
    print response.pretty_print()

def client_2_post(payload):
    response = client.put(path=path, payload=payload)
    print response.pretty_print()

def client_2_put(payload):
    response = client.put(path=path, payload=payload)
    print response.pretty_print()
