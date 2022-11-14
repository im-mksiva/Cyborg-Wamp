import asyncio
import time

from cyborg.conf import CONF as config
import json
import ssl
from threading import Thread
from time import sleep
import oslo_messaging
from autobahn.asyncio.component import Component
from autobahn.asyncio.component import run
from oslo_service import service
import oslo_config as cfg


from oslo_log import log as logging

LOG = logging.getLogger(__name__)


loop1 = asyncio.new_event_loop()
loop2 = asyncio.new_event_loop()

SESSION = None
COMMAND = None

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
whost = "localhost"
wport = 8181
wamp_transport = [
    {
        "url": "wss://localhost:8181/",
        "max_retries": -1,
        "serializers": ["json"],
        "endpoint": {"type": "tcp", "host": whost, "port": wport, "tls": ctx},
    },
]


async def wamp_request():
    LOG.info("ESECUZIONE TRAMITE WAMP")
    result = await SESSION.call("cyborg.program")

    return result.result()


#########################################################################################################################

# OSLO ENDPOINT
class Functions_to_wamp(object):
    def call_wamp(self, ctx):
        res = asyncio.run(wamp_request())
        return res


class RPCServer(Thread):
    def __init__(self):

        endpoints = [Functions_to_wamp()]

        Thread.__init__(self)
        transport = oslo_messaging.get_rpc_transport(config)

        target = oslo_messaging.Target(exchange="cyborg", topic="test", server="server")
        self.server = oslo_messaging.get_rpc_server(
            transport, target, endpoints, executor="threading"
        )

    def run(self):
        LOG.info("Avvio AMQP server... ")
        self.server.start()

    def stop(self):
        LOG.info("AMQP server in arresto... ")
        self.server.stop()
        LOG.info("AMQP server fermato. ")


#########################################################################################################################


class WampAgent:
    def __init__(self):
        self.comp = Component(
            transports=wamp_transport,
            realm="s4t",
        )
        self.session = SESSION

        @self.comp.on_join
        async def OnJoin(session, details):
            print("connessione stabilita")

            try:
                print("assegnazione di session")
                self.session = session
                global SESSION
                SESSION = session
            except Exception as e:
                print("call error: {0}".format(e))

    def start(self):
        # run([self.comp])
        loop3 = asyncio.new_event_loop()
        asyncio.set_event_loop(loop3)
        # self.comp.start(loop3)
        run([self.comp])
        # self.comp.fire
        print("component avviato")
        return self.comp


def start_wamp():
    esempio = WampAgent()
    esempio.start()
    return esempio


server = RPCServer()
server_thread = Thread(None, server.start)
server_thread.start()
start_wamp()

