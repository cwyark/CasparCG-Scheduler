import web
import settings
import sys
from models import ModelHandler
from twisted.web.wsgi import WSGIResource
from twisted.web.server import Site
from twisted.internet import reactor, protocol
from twisted.python import log


class AMCPHandler(object):

    def __init__(self):
        pass


class AMCPProtocol(protocol.Protocol):
    def connectionMade(self):
        log.msg("connect with server %s build" % self.transport.getPeer())
        # self.transport.write("CLS\r\n")

    def dataReceived(self, data):
        log.msg("%s" % data)


class AMCPFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return AMCPProtocol()

    def clientConnectionFailed(self, connector, reason):
        print "Connection between server failed, reason :%s" % reason

    def clientConnectionLost(self, connector, reason):
        print "Connection between server lost, reason :%s" % reason


# register a web for twisted's WSGI application
resource = WSGIResource(reactor, reactor.getThreadPool(), web.app)
site = Site(resource)


if __name__ == "__main__":
    log.startLogging(sys.stdout)
    model = ModelHandler()
    reactor.listenTCP(settings.__WEBCLIENT_PORT__, site)
    reactor.connectTCP(settings.__CASPARCG_SERVER_IP__, settings.__CASPARCG_SERVER_PORT__, AMCPFactory())
    reactor.run()
