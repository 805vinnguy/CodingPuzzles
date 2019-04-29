#!/usr/bin/env python3

import unittest
from solution import *

class Test(unittest.TestCase):

    def test_1(self):
        N = 4
        X = (1, 2)
        result = 5
        self.assertEqual(count_ways(N, X), result)

if __name__ == "__main__":
    unittest.main()
