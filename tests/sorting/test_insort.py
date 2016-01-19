import unittest

from algs.sorting.insort import insertion_sort


class TestInsort(unittest.TestCase):

    def setUp(self):
        self.test_arr = [8, 1, 3, 2, 7, 1, 2, 9, 0, 8, 14, -22]

    def is_sorted(self, arr, upto):
        for i in range(upto):
            if arr[i] <= arr[i + 1]:
                continue  # ok
            else:
                return False
        return True

    def test_sort(self):
        insertion_sort(self.test_arr)
        self.assertTrue(self.is_sorted(self.test_arr, len(self.test_arr) - 1))
