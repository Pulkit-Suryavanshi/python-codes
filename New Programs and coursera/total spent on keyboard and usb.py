#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, s):
    keyboards.sort(reverse=True)
    drives.sort()
    res = -1
    for k in keyboards:
        for d in drives:
            if k+d > s:
                break
            if k+d > res:
                res = k+d
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
"""THIS IS MY CODE NOT RUNNING ## TEST CASES

#!/bin/python3
# sum of the two list items must be less than budget else print -1 or print the max price
import os
import sys


#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    max = 0
    t = 0
    count = 0
    for i in keyboards:
        for j in drives:
            t = i + j
            if (t > max and t < b):
                max = t
                count = 1
            else:
                pass
    if (count == 1):
        print(max)
    else:
        print(-1)


if __name__ == '__main__':
    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    getMoneySpent(keyboards, drives, b)"""
