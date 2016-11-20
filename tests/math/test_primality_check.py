import unittest
from algs.math.primality_check import is_prime, is_prime2


class TestIsPrime(unittest.TestCase):

    def test_is_2_prime(self):
        self.assertTrue(is_prime(13))

    def test_is_3_prime(self):
        self.assertTrue(is_prime(3))

    def test_is_4_prime(self):
        self.assertFalse(is_prime(4))

    def test_is_5_prime(self):
        self.assertTrue(is_prime(5))

    def test_is_13_prime(self):
        self.assertTrue(is_prime(17))

    def test_is_22_prime(self):
        self.assertFalse(is_prime(22))


class TestIsPrime2(unittest.TestCase):

    def test_is_2_prime(self):
        self.assertTrue(is_prime2(13))

    def test_is_3_prime(self):
        self.assertTrue(is_prime2(3))

    def test_is_4_prime(self):
        self.assertFalse(is_prime2(4))

    def test_is_5_prime(self):
        self.assertTrue(is_prime2(5))

    def test_is_13_prime(self):
        self.assertTrue(is_prime2(17))

    def test_is_22_prime(self):
        self.assertFalse(is_prime2(22))
