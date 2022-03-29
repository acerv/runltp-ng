"""
Unit tests for metadata implementations.
"""
import pytest
from ltp.metadata import RuntestMetadata
from ltp.metadata import MetadataError


@pytest.fixture(autouse=True)
def create_suites(tmpdir):
    """
    Create testing suites.
    """
    root = tmpdir.mkdir("runtest")

    suitefile = root.join("suite01")
    suitefile.write("mytest01 mybin -a\n"
                    "mytest02 mybin -b\n"
                    "mytest03 mybin -c\n"
                    "mytest04 mybin -d\n")

    suitefile = root.join("suite02")
    suitefile.write("mytest05 mybin -a\n"
                    "mytest06 mybin -b\n"
                    "mytest07 mybin -c\n"
                    "mytest08 mybin -d\n")


class TestRuntestMetadata:
    """
    Test RuntestMetadata implementations.
    """

    def test_no_read_suite(self, tmpdir):
        """
        Test read_suite method.
        """
        meta = RuntestMetadata(str(tmpdir) + "/runtest")

        with pytest.raises(MetadataError):
            meta.read_suite("dirsuiteXYZ")

    def test_read_suite(self, tmpdir):
        """
        Test read_suite method.
        """
        meta = RuntestMetadata(str(tmpdir) + "/runtest")

        suite = meta.read_suite("suite01")

        assert suite.name == "suite01"
        assert suite.tests[0].name == "mytest01"
        assert suite.tests[0].command == "mybin"
        assert suite.tests[0].arguments == ['-a']

        assert suite.tests[1].name == "mytest02"
        assert suite.tests[1].command == "mybin"
        assert suite.tests[1].arguments == ['-b']

        assert suite.tests[2].name == "mytest03"
        assert suite.tests[2].command == "mybin"
        assert suite.tests[2].arguments == ['-c']

        assert suite.tests[3].name == "mytest04"
        assert suite.tests[3].command == "mybin"
        assert suite.tests[3].arguments == ['-d']

        suite = meta.read_suite("suite02")

        assert suite.name == "suite02"
        assert suite.tests[0].name == "mytest05"
        assert suite.tests[0].command == "mybin"
        assert suite.tests[0].arguments == ['-a']

        assert suite.tests[1].name == "mytest06"
        assert suite.tests[1].command == "mybin"
        assert suite.tests[1].arguments == ['-b']

        assert suite.tests[2].name == "mytest07"
        assert suite.tests[2].command == "mybin"
        assert suite.tests[2].arguments == ['-c']

        assert suite.tests[3].name == "mytest08"
        assert suite.tests[3].command == "mybin"
        assert suite.tests[3].arguments == ['-d']
