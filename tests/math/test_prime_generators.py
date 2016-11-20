import unittest
from algs.math.prime_generators import generate_primes_upto


class TestGeneratePrimesUpto(unittest.TestCase):

    def test_generate_primest_upto_23(self):
        real_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        generated = generate_primes_upto(23)
        self.assertEqual(generated, real_primes)
