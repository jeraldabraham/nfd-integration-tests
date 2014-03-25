#!/usr/bin/python
import unittest

class test_ndn_tlv_poke(unittest.TestCase):

    def setUp(self):
        print "ndn-tlv-poke - Setup Complete"

    def tearDown(self):
        print "ndn-tlv-poke - Tear Down Complete"

    def test_poke(self):
        self.assertEqual(1, 2, "ndn-tlv-poke - Test Failed")

if __name__ == "__main__":
    unittest.main()
