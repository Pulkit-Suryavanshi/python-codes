#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):
    w=0          #no. of wrapper
    c=int(n/c)   #no. of chocolates
    w=c          #no. of chocolates is equal to no. of wrapper
    while w>=m:
        c+=int(w/m)
        w=int(w/m)+(w%m)
    return(c)    #this returns no. of chocolates

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
