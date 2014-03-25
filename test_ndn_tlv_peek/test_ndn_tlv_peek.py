#!/usr/bin/python
import unittest

class test_ndn_tlv_peek(unittest.TestCase):

    def setUp(self):
        print "ndn-tlv-peek - Setup Complete"

    def tearDown(self):
        print "ndn-tlv-peek - Tear Down Complete"

    def test_peek(self):
        self.assertEqual(1, 2, "ndn-tlv-peek - Test Failed")

if __name__ == "__main__":
    unittest.main()
