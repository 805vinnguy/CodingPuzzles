#!/usr/bin/env python3

import unittest
import ksum

class TestKSum(unittest.TestCase):

    def test_1(self):
        numbers = [10, 15, 3, 7]
        k = 17
        self.assertTrue(ksum.k_sum(numbers, k))

    def test_endtrue(self):
        numbers = [9, 15, 3, 7]
        k = 10
        self.assertTrue(ksum.k_sum(numbers, k))

    def test_false(self):
        numbers = [3, 7, 1, 4]
        k = 15
        self.assertFalse(ksum.k_sum(numbers, k))

    def test_negative(self):
        numbers = [-4, 9, -3, 20]
        k = 17
        self.assertTrue(ksum.k_sum(numbers, k))

    def test_zero(self):
        numbers = [0, -10, 10, 0]
        k = 0
        self.assertTrue(ksum.k_sum(numbers, k))

if __name__ == "__main__":
    unittest.main()
