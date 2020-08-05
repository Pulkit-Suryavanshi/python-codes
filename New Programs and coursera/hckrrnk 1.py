#!/bin/python3
#count no. of birds seen that is common and is smaller index
import math
import os
import random
import re
import sys


# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    seen = [0, 0, 0, 0, 0]
    for i in arr:
        if (i == 1):
            seen[0] = seen[0] + 1
        elif (i == 2):
            seen[1] = seen[1] + 1
        elif (i == 3):
            seen[2] = seen[2] + 1
        elif (i == 4):
            seen[3] = seen[3] + 1
        elif (i == 5):
            seen[4] = seen[4] + 1
    x = max(seen)
    ind = seen.index(x)
    indp = ind + 1
    print(indp)


if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)
