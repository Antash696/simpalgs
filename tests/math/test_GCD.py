import unittest
from algs.math.GCD import GCD


class TestGCD(unittest.TestCase):

    def setUp(self):
        pass

    def test_GCD_equal(self):
        self.assertEqual(GCD(7, 7), 7)

    def test_GCD_prime(self):
        self.assertEqual(GCD(17, 6), 1)

    def test_GCD_two_primes(self):
        self.assertEqual(GCD(17, 7), 1)

    def test_GCD_even(self):
        self.assertEqual(GCD(18, 6), 6)
