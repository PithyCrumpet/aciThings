import unittest
from login import *
from aciUrls import *

class urlsTestCase(unittest.TestCase):
    """Tests for `aciUrls`."""

    def testGetSwitchportDetailsUrl(self):
        """Does getSwitchportDetailsUrl return switchport info ?"""
        token = login('sandboxapicdc.cisco.com', 'admin', 'ciscopsdt')
        urls = urlList()
        self.assertTrue(urls.getRequest(urls.getSwitchportDetailsUrl('sandboxapicdc.cisco.com', '1', '101', 'eth1/1'), token))

if __name__ == '__main__':
    unittest.main()