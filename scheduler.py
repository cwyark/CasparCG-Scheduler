from twisted.internet import reactor, protocol


class EchoClient(protocol.Protocol):
    def connectionMade(self):
        self.transport.write("INFO\r\n")

    def dataReceived(self, data):
        print "Server said:", data


class EchoFactory(protocol.ClientFactory):

    def buildProtocol(self, addr):
        return EchoClient()

    def clientConnectionFailed(self, connector, reason):
        print "Connect failed, reason:" + reason
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print "Connect loss, reason:" + reason
        reactor.stop()

reactor.connectTCP("192.168.144.16", 5250, EchoFactory())
reactor.run()
