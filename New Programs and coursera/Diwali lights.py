#!/bin/python3

import os
import sys

#
# Complete the lights function below.
#
def lights(n):
    return ((2**n)-1)%100000
#Print the total number of patterns modulo 10^5
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = lights(n)

        fptr.write(str(result) + '\n')

    fptr.close()
'''Suppose X = "off" and O = "on". Let's define the possible lighting
setups for 1, 2, 3 lights and see if we are able to identify any pattern:
1 - O, X (2 patterns)

2 - OO, OX, XO, XX (4 patterns)

3 - OOO, OXO, OOX, XOO, XXO, OXX, XOX, XXX (8 patterns)
You notice how you get 2^n patterns for any number of lights. Since you know
that at least one light is on at any time, you have to exclude
the pattern in which all lights are off, so you just subtract one from it.
Which means that the solution is: (2**n) - 1'''