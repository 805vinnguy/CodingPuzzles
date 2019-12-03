#!/usr/bin/env python3

import unittest
from transcribe import matchNames

class Test_matchNames(unittest.TestCase):

    def test_basic_0(self):
        inputNames = ["Courtney Mackstutis", "Angela Gimbel", "Hector Koba"]
        dmvRecords = ["Courtney Mackstutis;4766 Moctezuma", "Angela Gimbel;1270 Finazzo", "Hector Koba;7074 Turrill"]
        expected = ["4766 Moctezuma", "1270 Finazzo", "7074 Turrill"]
        self.assertEqual(matchNames(inputNames, dmvRecords), expected)

    def test_misspellings_0(self):
        inputNames = ["Courtnet Mackstutis", "Angela Gimbrel", "Hector Kba"]
        dmvRecords = ["Courtney Mackstutis;4766 Moctezuma", "Angela Gimbel;1270 Finazzo", "Hector Koba;7074 Turrill"]
        expected = ["4766 Moctezuma", "1270 Finazzo", "7074 Turrill"]
        self.assertEqual(matchNames(inputNames, dmvRecords), expected)

if __name__ == "__main__":
    unittest.main()
