import unittest
from login import *

class urlsTestCase(unittest.TestCase):
    """Tests for `login`."""

    def testGetSwitchportDetailsUrl(self):
        """Does login successfully login ?"""
        self.assertTrue(login('sandboxapicdc.cisco.com', 'admin', 'ciscopsdt'))

if __name__ == '__main__':
    unittest.main()