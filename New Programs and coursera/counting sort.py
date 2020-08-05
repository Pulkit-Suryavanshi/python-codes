n = input()
ans = [0] * 100
for i in [int(n) for n in input().split()]:
    ans[i] += 1
print(*ans)