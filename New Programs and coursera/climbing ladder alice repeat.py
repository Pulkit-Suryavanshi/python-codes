#!/bin/python3
from collections import Counter
import os

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    res=[]
    b=list(Counter(scores).keys())
    c = list(Counter(scores))
    print(b)
    temp=len(b)-1
    for a in alice:
        for i in range(temp,-1,-1):
            print(b[i],i)
            if b[i]>a:
                res.append(i+2)
                temp=i
                break
            elif i==0:
                res.append(1)
    return res

if __name__ == '__main__':
    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))
    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)
    print(result)