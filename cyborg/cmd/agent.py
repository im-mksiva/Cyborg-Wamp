#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""The Cyborg Agent Service."""

import shlex
import sys

from oslo_config import cfg
from oslo_privsep import priv_context
from oslo_service import service

from cyborg.common import constants
from cyborg.common import service as cyborg_service

CONF = cfg.CONF


def main():
    # Parse config file and command line options, then start logging
    cyborg_service.prepare_service(sys.argv)
    priv_context.init(root_helper=shlex.split('sudo'))

    mgr = cyborg_service.RPCService('cyborg.agent.wamp',
                                    'WampService',
                                    constants.AGENT_TOPIC)
    # mgr.start()
    # launcher = service.launch(CONF, mgr, restart_method='mutate')
    # launcher.wait()
