from coapthon.client.helperclient import HelperClient

client = None
path = "basic"


def client_1_connect():
    global client
    host = "127.0.0.1"
    port = 5683
    client = HelperClient(server=(host, port)) #Connection to server

def client_1_stop():
    print "\n\n"
    print "Stoping..."
    client.stop()

def client_1_get():
    response = client.get(path=path)
    print "\n\n"
    print response.pretty_print()

def client_1_post(payload):
    response = client.put(path=path, payload=payload)
    print "\n\n"
    print response.pretty_print()

def client_1_put(payload):
    response = client.put(path=path, payload=payload)
    print "\n\n"
    print response.pretty_print()

def client_1_delete():
    response = client.delete(path)
    print "\n\n"
    print response.pretty_print()

def main():
    client_1_connect()
    while True:
        print "Press 1, to GET:"
        print "Press 2, to PUT:"
        print "Press 3, to POST:"
        print "Press 4, to DELETE:\n"
        input = int(raw_input("Enter your choice: "))

        if input == 1:
            client_1_get()

        elif input == 2:
            print "PUT"
            message = str(raw_input("Enter message: "))
            client_1_put(message)

        elif input == 3:
            print "POST"
            message = str(raw_input("Enter message: "))
            client_1_post(message)

        elif input == 4:
            print "DELETE"
            client_1_delete()
        else:
            break

    client_1_stop()

if __name__ == '__main__':
    main()