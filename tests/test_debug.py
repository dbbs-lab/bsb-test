import unittest

from bsb_test import ConfigFixture, NetworkFixture, NumpyTestCase, RandomStorageFixture


class TestChunked(
    RandomStorageFixture,
    ConfigFixture,
    NetworkFixture,
    NumpyTestCase,
    unittest.TestCase,
    config="chunked",
    engine_name="hdf5",
):
    def setUp(self):
        super().setUp()
        self.network.compile(clear=True)

    def test_fixed_connectivity(self):
        cs = self.network.get_connectivity_set("A_to_B")

        pre, post = cs.load_connections().all()
        self.assertClose(
            [
                [0, 0, 0],
                [1, 0, 0],
                [5, 0, 0],
                [1, 0, 0],
                [3, 0, 0],
                [5, 0, 0],
                [5, 0, 0],
                [5, 0, 0],
                [5, 0, 0],
                [1, 0, 0],
                [5, 0, 0],
            ],
            pre,
        )

        self.assertClose(
            [
                [0, 0, 0],
                [0, 0, 0],
                [2, 0, 0],
                [3, 0, 0],
                [8, 0, 0],
                [9, 0, 0],
                [10, 0, 0],
                [11, 0, 0],
                [1, 0, 0],
                [5, 0, 0],
                [11, 0, 0],
            ],
            post,
        )