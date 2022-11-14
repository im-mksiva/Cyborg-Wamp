import pecan
from wsme import types as wtypes

from cyborg.agent.rpcapi import AgentAPI
from cyborg.api.controllers import base
from cyborg.api import expose

from oslo_log import log

LOG = log.getLogger(__name__)


class ProgramController(base.CyborgController):
    """REST controller for programming FPGAs."""

    _custom_actions = {'program': ['POST']
                        }

    @expose.expose(wtypes.text)
    def program(self):
        """Program a FPGA."""

        # cyborg-agent/rpcapi.py contiene il metodo fpga_program tramite il quale effettuo la RPC
        self.agent_rpcapi = AgentAPI()
        ret = self.agent_rpcapi.fpga_program(
            pecan.request.context
            )
            
        return ret
