"""
.. module:: __init__
    :platform: Linux
    :synopsis: SUT package definition

.. moduleauthor:: Andrea Cervesato <andrea.cervesato@suse.com>
"""
from .base import SUT
from .base import SUTError
from .base import SUTTimeoutError
from .host import HostSUT
from .qemu import QemuSUT
from .ssh import SSHSUT

__all__ = [
    "SUT",
    "SUTError",
    "SUTTimeoutError",
    "HostSUT",
    "QemuSUT",
    "SSHSUT",
]
