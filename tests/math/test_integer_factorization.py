import unittest
from algs.math.integer_factorization import prime_factors


class PrimeFactors(unittest.TestCase):

    def test_prime_factors_low_prime(self):
        factors = [2]
        result = prime_factors(2)
        self.assertEqual(result, factors)

    def test_prime_factors_low(self):
        factors = [2, 3]
        result = prime_factors(6)
        self.assertEqual(result, factors)

    def test_prime_factors_med(self):
        factors = [2, 3, 3, 13]
        result = prime_factors(234)
        self.assertEqual(result, factors)

    def test_prime_factors_prime(self):
        factors = [127]
        result = prime_factors(127)
        self.assertEqual(result, factors)

    def test_prime_factors_semi_prime(self):
        factors = [13, 127]
        result = prime_factors(1651)
        self.assertEqual(result, factors)
