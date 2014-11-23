import web
import settings
import models
import sys
from twisted.web.wsgi import WSGIResource
from twisted.web.server import Site
from twisted.internet import reactor, protocol
from twisted.python import log


class AMCPProtocol(protocol.Protocol):
    def connectionMade(self):
        print "connect with server %s build" % self.transport.getPeer()
        self.transport.write("INFO\r\n")

    def dataReceived(self, data):
        print "CasparCG Server: %s" % data


class AMCPFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return AMCPProtocol()

    def clientConnectionFailed(self, connector, reason):
        print "Connection with server failed, reason :%s" % reason

    def clientConnectionLost(self, connector, reason):
        print "Connection with server lost, reason :%s" % reason


# register a web for twisted's WSGI application
resource = WSGIResource(reactor, reactor.getThreadPool(), web.app)
site = Site(resource)


if __name__ == "__main__":
    log.startLogging(sys.stdout)
    models.database_init()
    reactor.listenTCP(settings.__WEBCLIENT_PORT__, site)
    reactor.connectTCP(settings.__CASPARCG_SERVER_IP__, settings.__CASPARCG_SERVER_PORT__, AMCPFactory())
    reactor.run()
