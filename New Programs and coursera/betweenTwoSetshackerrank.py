import sys
from fractions import gcd

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
A = map(int,input().strip().split(' '))
B = map(int,input().strip().split(' '))

def LCM(a, b):
    return (a*b)//gcd(a,b)

lcm = reduce(LCM, A, 1)
gcd = reduce(gcd, B)

lcm_copy = lcm

count = 0
while lcm <= gcd:
    if(gcd % lcm) == 0:
        count += 1
    lcm = lcm + lcm_copy

print(count)


'''
import sys
from functools import reduce
from fractions import gcd

input()
a = map(int,input().strip().split())
b = map(int,input().strip().split())
lcm_a = reduce(lambda x,y: x*y//gcd(x,y), a)
gcd_b = reduce(gcd, b)
print(sum(1 for x in range(lcm_a,gcd_b+1,lcm_a) if gcd_b%x==0))

quest:
You will be given two arrays of integers and asked to determine all integers that satisfy the following two conditions:

1.The elements of the first array are all factors of the integer being considered
2.The integer being considered is a factor of all elements of the second array
These numbers are referred to as being between the two arrays. You must determine how many such numbers exist.

'''