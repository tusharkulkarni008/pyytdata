import datetime
import os
import unittest

from pyytdata import PyYtData


class TestPyYtData(unittest.TestCase):
    def test_check_env(self):
        self.assertTrue(os.environ.get("API_KEY") is not None)

    def setUp(self):
        self.data = PyYtData("flask", 1)
        self.rslt = self.data.get_videoinfo()

    def test_get_videoinfo(self):
        self.assertTrue(len(self.rslt) == 1)


if __name__ == "__main__":
    unittest.main()
