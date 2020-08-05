#!/bin/python3
# pair according to color and print how many pairs
import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ans=list()
    counting=list()
    for i in ar:
        if not i in counting:
            counting.append(i)
            counti=ar.count(i)
            pairs=counti//2
            ans.append(pairs)
    return sum(ans)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()