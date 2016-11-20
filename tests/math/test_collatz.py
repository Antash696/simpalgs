import unittest
from algs.math.collatz import collatz_length, collatz_seq


class TestCollatzLenght(unittest.TestCase):

    def setUp(self):
        self.memo = {2: 1}

    def test_collatz_lenght_1(self):
        start = 2
        self.assertEqual(collatz_length(start, self.memo), 1)

    def test_collatz_lenght_2(self):
        start = 9
        self.assertEqual(collatz_length(start, self.memo), 19)

    def test_collatz_lenght_3(self):
        start = 10
        self.assertEqual(collatz_length(start, self.memo), 6)


class TestCollatzSeq(unittest.TestCase):

    def test_collatz_seq_1(self):
        start = 2
        seq = [2, 1]
        self.assertEqual(collatz_seq(start), seq)

    def test_collatz_seq_2(self):
        start = 9
        seq = [9, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        self.assertEqual(collatz_seq(start), seq)

    def test_collatz_seq_3(self):
        start = 10
        seq = [10, 5, 16, 8, 4, 2, 1]
        self.assertEqual(collatz_seq(start), seq)
