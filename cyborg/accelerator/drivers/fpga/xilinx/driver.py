# """
# Cyborg Xilinx FPGA driver implementation.
# """

# from oslo_log import log as logging

# from oslo_concurrency import processutils
# from cyborg.accelerator.drivers.fpga.base import FPGADriver
# from cyborg.accelerator.drivers.fpga.xilinx import sysinfo

# LOG = logging.getLogger(__name__)


# class XilinxFPGADriver(FPGADriver):
#     """Class for Xilinx FPGA drivers.
#        Vendor should implement their specific drivers in this class.
#     """
#     VENDOR = "xilinx"

#     def __init__(self, *args, **kwargs):
#         pass

#     def program():
#         cmd = ["sudo", "xc3sprog", "-c", "nexys4", "/home/me/top.bit"]
#         result = processutils.execute(*cmd)
#         return "programmazione dal driver xilinx"



#     def discover(self):
#         return sysinfo.fpga_tree()

# Copyright 2018 Lenovo, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


"""
Cyborg Xilinx FPGA driver implementation.
"""
from oslo_concurrency import processutils
from cyborg.accelerator.drivers.fpga.base import FPGADriver
from cyborg.accelerator.drivers.fpga.xilinx import sysinfo


class XilinxFPGADriver(FPGADriver):
    """Base class for Xilinx FPGA drivers.

       This is just a virtual Xilinx FPGA drivers interface.
       Vedor should implement their specific drivers.
    """

    VENDOR = "xilinx"

    def __init__(self, *args, **kwargs):
        pass

    def discover(self):
        return sysinfo.fpga_tree()

    def program(self):
        cmd = ["ls", "-l"]
        result = processutils.execute(*cmd)
        return "programmazione dal driver xilinx"

    def check_program_status(self, device):
        return sysinfo.verify(device.pcie_address)

    def get_function(self, device):
        return sysinfo.get_function(device.pcie_address)
