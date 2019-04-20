#!/usr/bin/env python3

import unittest
import productarray

class TestProductArray(unittest.TestCase):

    def test_1_no_div(self):
        input_arr = [1, 2, 3, 4, 5]
        expect = [120, 60, 40, 30, 24]
        output_arr = productarray.product_array_no_div(input_arr)
        self.assertEqual(output_arr, expect)

    def test_2_no_div(self):
        input_arr = [3, 2, 1]
        expect = [2, 3, 6]
        output_arr = productarray.product_array_no_div(input_arr)
        self.assertEqual(output_arr, expect)

    def test_1_div(self):
        input_arr = [1, 2, 3, 4, 5]
        expect = [120, 60, 40, 30, 24]
        output_arr = productarray.product_array_no_div(input_arr)
        self.assertEqual(output_arr, expect)

    def test_2_div(self):
        input_arr = [3, 2, 1]
        expect = [2, 3, 6]
        output_arr = productarray.product_array_no_div(input_arr)
        self.assertEqual(output_arr, expect)

if __name__ == "__main__":
    unittest.main()
