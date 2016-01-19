import unittest

from algs.sorting.insort import insertion_sort


class TestInsort(unittest.TestCase):

    def setUp(self):
        self.test_arr_mixed = [8, 1, 3, 2, 7, 1, 2, 9, 0, 8, 14, -22]
        self.test_arr_negs = [-6, -3, -9, -22, 0, -1, -6]

    def is_sorted(self, arr, upto):
        for i in range(upto):
            if arr[i] <= arr[i + 1]:
                continue  # ok
            else:
                return False
        return True

    def test_sort_mixed(self):
        insertion_sort(self.test_arr_mixed)
        self.assertTrue(self.is_sorted(self.test_arr_mixed, len(self.test_arr_mixed) - 1))

    def test_sort_negs(self):
        insertion_sort(self.test_arr_negs)
        self.assertTrue(self.is_sorted(self.test_arr_negs, len(self.test_arr_negs) - 1))
