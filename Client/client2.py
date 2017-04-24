from coapthon.client.helperclient import HelperClient

client = None
path = "basic"


def client_2_connect():
    global client
    host = "127.0.0.1"
    port = 5683
    client = HelperClient(server=(host, port)) #Connection to server


def client_2_stop():
    print "\n\n"
    print "Stoping..."
    client.stop()

def client_2_get():
    response = client.get(path=path)
    print "\n\n"
    print response.pretty_print()

def client_2_post(payload):
    response = client.put(path=path, payload=payload)
    print "\n\n"
    print response.pretty_print()

def client_2_put(payload):
    response = client.put(path=path, payload=payload)
    print "\n\n"
    print response.pretty_print()


def client_2_delete():
    response = client.delete(path=path)
    print "\n\n"
    print response

def main():
    client_2_connect()
    while True:
        print "Press 1, to GET:"
        print "Press 2, to PUT:"
        print "Press 3, to POST:"
        print "Press 4, to DELETE:\n"
        input = int(raw_input("Enter your choice: "))

        if input == 1:
            client_2_get()

        elif input == 2:
            print "PUT"
            message = str(raw_input("Enter message: "))
            client_2_put(message)

        elif input == 3:
            print "POST"
            message = str(raw_input("Enter message: "))
            client_2_post(message)

        elif input == 4:
            print "DELETE"
            client_2_delete()
        else:
            break

    client_2_stop()

if __name__ == '__main__':
    main()