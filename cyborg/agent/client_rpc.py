import oslo_messaging as messaging
from oslo_config import cfg

CONF = cfg.CONF


class TestClient(object):
    def __init__(self):
        transport = messaging.get_rpc_transport(cfg.CONF)
        target = messaging.Target(topic="test", version="1.0")
        self.client = messaging.RPCClient(transport, target)

    def test(self):
        return self.client.call({}, "call_wamp")

    def stampa(self):
        print("Funziona?")

    def get_conf(self):
        return CONF


def chiamata():
    caller = TestClient()
    caller.test()
    return "test riuscito"




esempio = TestClient()
print(esempio.test())
