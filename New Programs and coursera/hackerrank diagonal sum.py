n = int(input())
arr = []
for i in range(0, n):
    arr.append([int(j) for j in input().split()])
d1 = 0
d2 = 0         #j
#  0  1  2  i-->|
#0 2  3  4      |
#1 4  5  2     \/
#2 6  1  2   therefore ||2+3+5|-|4+5+6||=5
for i in range(0, n):
    for j in range(0, n):
        if (i == j):
            d1 += arr[i][j]
        if (i == n - j - 1):
            d2 += arr[i][j]

y = abs(d1 - d2)
print(y)