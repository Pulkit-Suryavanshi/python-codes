#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a):
    j=1
    for i in a:
        if(j<=len(a)):
            print(a[-(j)],end=" ")
            j+=1

if __name__ == '__main__':
    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

