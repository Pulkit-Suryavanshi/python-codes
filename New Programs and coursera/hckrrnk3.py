#!/bin/python3
#share chocolate according to month span and day sum
import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(n, s, d, m):
    count = 0
    for i in range(0,n):
        total = sum(s[i:m+i])
        if total == d:
            count+=1
    print(count)

if __name__ == '__main__':
    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(n,s, d, m)
