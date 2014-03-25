#!/usr/bin/python
import unittest

class test_ndn_traffic_generator(unittest.TestCase):

    def setUp(self):
        print "ndn-traffic-generator - Setup Complete"

    def tearDown(self):
        print "ndn-traffic-generator - Tear Down Complete"

    def test_traffic(self):
        self.assertEqual(1, 2, "ndn-traffic-generator - Test Failed")

if __name__ == "__main__":
    unittest.main()
