"""
.. module:: local
    :platform: Linux
    :synopsis: module containing SUT definition for local testing execution

.. moduleauthor:: Andrea Cervesato <andrea.cervesato@suse.com>
"""
from ltp.runner import Runner
from ltp.runner import ShellRunner
from ltp.downloader import Downloader
from ltp.downloader import LocalDownloader
from .base import SUT
from .base import SUTError
from .base import SUTFactory


class LocalSUT(SUT):
    """
    Local SUT implementation for host testing.
    """

    def __init__(self) -> None:
        self._downloader = None
        self._runner = None

    @property
    def name(self) -> str:
        return "host"

    @property
    def downloader(self) -> Downloader:
        return self._downloader

    @property
    def runner(self) -> Runner:
        return self._runner

    def communicate(self, stdout_callback: callable = None) -> None:
        if self._downloader or self._runner:
            raise SUTError("SUT is already running")

        self._downloader = LocalDownloader()
        self._runner = ShellRunner()

    def stop(self) -> None:
        self._runner.stop()
        self._downloader.stop()

    def force_stop(self) -> None:
        self._runner.force_stop()
        self._downloader.stop()


class LocalSUTFactory(SUTFactory):
    """
    LocalSUT factory class.
    """

    def create(self) -> SUT:
        sut = LocalSUT()
        return sut