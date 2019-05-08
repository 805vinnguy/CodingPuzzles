#!/usr/bin/env python3

import math
import os
import random
import re
import sys
import transcribe

def main():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    inputNames_count = int(input().strip())

    inputNames = []

    for _ in range(inputNames_count):
        inputNames_item = input()
        inputNames.append(inputNames_item)

    dmvRecords_count = int(input().strip())

    dmvRecords = []

    for _ in range(dmvRecords_count):
        dmvRecords_item = input()
        dmvRecords.append(dmvRecords_item)

    res = transcribe.matchNames(inputNames, dmvRecords)

    fptr.write('\n'.join(res))
    fptr.write('\n')

    fptr.close()

if __name__ == "__main__":
    main()

# END OF FILE
