from coapthon.server.coap import CoAP
from coapthon.resources.resource import Resource

server = None
resource = None

class BasicResource(Resource):
    def __init__(self, name="BasicResource", coap_server=None):
        super(BasicResource, self).__init__(name, coap_server, visible=True,observable=True, allow_children=True)
        self.payload = "basic Res"

    def render_GET(self, request):
        return self

    def render_PUT(self, request):
        self.payload = request.payload
        return self

    def render_POST(self, request):
        res = BasicResource()
        res.location_query = request.uri_query
        res.payload = request.payload
        return res

    def render_DELETE(self, request):
        return True

class CoAPServer(CoAP):
    def __init__(self, host, port):
        global resource
        CoAP.__init__(self, (host, port))
        resource = BasicResource()
        resource.resource_type
        self.add_resource('basic/', resource)

def get_server():
    global server
    server = CoAPServer("0.0.0.0", 5683)
    try:
        server.listen(10)
    except KeyboardInterrupt:
        print "Server Shutdown"
        server.close()
        print "Exiting..."

def get_server_payload():
    return resource.payload

def get_server_type():
    return resource.resource_type

def get_server_mid():
    pass
    #return resource

if __name__ == '__main__':
    get_server()