from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    return Response('Hello %(name)s!' % request.matchdict)

if __name__=='__main__':
    print 'server is on'
    print 'address is http://0.0.0.0:6000'
    import pdb;pdb.set_trace()
    config = Configurator()
    config.add_route('hello','/hello/{name}')
    config.add_view(hello_world, route_name='hello')
    app = config.make_wsgi_app()
    server = make_server('127.0.0.1', 6000, app)
    server.serve_forever()

