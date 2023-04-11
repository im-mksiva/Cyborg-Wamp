

from autobahn.asyncio.component import Component, run
from autobahn.wamp.types import RegisterOptions
from autobahn import wamp

import asyncio
import ssl


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
        "endpoint": {
            "type": "tcp",
            "host": whost,
            "port": wport,
            "tls": ctx
            },
        },
    ]

component = Component(
    transports=wamp_transport,
    realm="s4t"
)

# @component.register
def funzione():
    print("esecuzione della funzione tramite Cyborg-WAMP")
    return str("ho eseguito la funzione, risultato tramite wamp")

@component.on_join
def start(session, details):
    print("connessione stabilita")
    try:
        # bastardo "yield from"
        yield from session.register(funzione,u'server.funzione')
        print("funzione aggiunta")
    except Exception as e:
        print("could not register procedure: {0}".format(e))



if __name__ == "__main__":
    run([component])
    