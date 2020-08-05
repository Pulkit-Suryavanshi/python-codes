#!/bin/python3
import os
import sys
'''to understand 621 540
n=11 p=4
Tlr=11/2  total to turn to end page
Plr=4/2 total pages turn if start from left
Prl=Tlr-Plr=5-2=3 '' if start from the right
min(Plr,Prl)=2
        int total = n/2;
        int right = p/2;
        int left = total - right;
        if(right < left){return right;}
        else {return left;}}'''
def pageCount(n, p):
    #print min(p/2,n/2-p/2) one liner
    counti = 0
    countj = 0
    for i in range(1, n + 1, 2):
        if (i >= p):
            break
        else:
            counti += 1
    for o in range(n, 0, -2):
        if (p in range(o - 1, o + 1)):
            break
        else:
            countj += 1
    if (counti < countj):
        print(counti)
    else:
        print(countj)


if __name__ == '__main__':
    n = int(input())

    p = int(input())

    pageCount(n, p)

