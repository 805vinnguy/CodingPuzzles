#!/usr/bin/env python3

import unittest
from solution import *

class Test(unittest.TestCase):

    def test_mono_inc(self):
        arr = [2, 4, 7]
        self.assertEqual(max_sum_non_adjacent(arr), 9)

    def test_ex_1(self):
        arr = [2, 4, 6, 2, 5]
        self.assertEqual(max_sum_non_adjacent(arr), 13)

    def test_ex_2(self):
        arr = [5, 1, 1, 5]
        self.assertEqual(max_sum_non_adjacent(arr), 10)

    def test_neg(self):
        arr = [-1, -9, 0, 3, -2]
        self.assertEqual(max_sum_non_adjacent(arr), 3)

if __name__ == "__main__":
    unittest.main()
