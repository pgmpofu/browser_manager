import unittest
from browser import *


class BrowserManagerTestCase(unittest.TestCase):
    def test_open_browser(self):
        self.assertRaises(Exception, open_website)


if __name__ == '__main__':
    unittest.main()
