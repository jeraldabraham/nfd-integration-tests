#!/usr/bin/python
import unittest

class test_ndn_tlv_ping(unittest.TestCase):

    def setUp(self):
        print "ndn-tlv-ping - Setup Complete"

    def tearDown(self):
        print "ndn-tlv-ping - Tear Down Complete"

    def test_ping(self):
        self.assertEqual(1, 2, "ndn-tlv-ping - Test Failed")

if __name__ == "__main__":
    unittest.main()
