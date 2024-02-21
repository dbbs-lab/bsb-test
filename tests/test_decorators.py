import unittest
from time import sleep

from bsb_test import timeout


class TestTimeout(unittest.TestCase):
    def test_timeout_regular(self):
        @timeout(1)
        def x():
            return 5

        x()

    def test_timeout_timeout(self):
        @timeout(1)
        def x():
            sleep(5)
            return 5

        with self.assertRaises(TimeoutError):
            x()

    def test_timeout_exception(self):
        @timeout(1)
        def x():
            raise ValueError()

        with self.assertRaises(ValueError):
            x()
