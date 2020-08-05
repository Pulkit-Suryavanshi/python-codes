#!/bin/python3

import math
import os
import random
import re
import sys
'''
n=no of prisioners
m=no of sweets
s=the seat no. to start giving sweets from
we have to warn the last person getting the sweet becoz the sweet if bad
ex: 5 2 1 gives ans 2
5 2 2 gives ans 3
7 19 2 gives 6
3 7 3 gives 3'''
# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    a=0
    a=(m+s-1)%n
    if a==0:
        return n
    else:
        return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
