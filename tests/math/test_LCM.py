import unittest
from algs.math.LCM import LCM, LCM2


class TestLCM(unittest.TestCase):

    def setUp(self):
        pass

    def test_LCM_equal(self):
        self.assertEqual(LCM(7, 7), 7)

    def test_LCM_prime(self):
        self.assertEqual(LCM(17, 6), 102)

    def test_LCM_two_primes(self):
        self.assertEqual(LCM(17, 7), 119)

    def test_LCM_even(self):
        self.assertEqual(LCM(18, 6), 18)


class TestLCM2(unittest.TestCase):

    def setUp(self):
        pass

    def test_LCM2_equal(self):
        self.assertEqual(LCM2(7, 7), 7)

    def test_LCM2_prime(self):
        self.assertEqual(LCM2(17, 6), 102)

    def test_LCM2_two_primes(self):
        self.assertEqual(LCM2(17, 7), 119)

    def test_LCM2_even(self):
        self.assertEqual(LCM2(18, 6), 18)
