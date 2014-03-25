#!/usr/bin/python
import unittest

class test_nfd_status(unittest.TestCase):

    def setUp(self):
        print "nfd-status - Setup Complete"

    def tearDown(self):
        print "nfd-status - Tear Down Complete"

    def test_status(self):
        self.assertEqual(1, 2, "nfd-status - Test Failed")

if __name__ == "__main__":
    unittest.main()
