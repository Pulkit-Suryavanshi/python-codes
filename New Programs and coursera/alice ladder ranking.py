import math
import os
import random
import re
import sys
# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice, scores_count, alice_count):
    rank = 1
    this = scores[0]
    prev = 0
    z=len(alice)
    for x, y in zip(alice,scores ):
        rank=1
        for ct in range(z):
            if (x < y) and (this != prev):
                prev = this
                this = scores[ct+1]
                rank = ct+1
            elif (x < y) and (this == prev):
                this=scores[ct+1]
                prev=this
                pass
        print(rank)


if __name__ == '__main__':
    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice, scores_count, alice_count)
