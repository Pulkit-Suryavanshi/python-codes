#python 3
#stack input append if 1 remove if 2 print if 3
items = [0]
for i in range(int(input())):
    nums = list(map(int, input().split()))
    if nums[0] == 1:
        items.append(max(nums[1], items[-1]))
    elif nums[0] == 2:
        items.pop()
    else:
        print(items[-1])
"""10
1 97
2
1 20
2
1 26
1 20
2
3
1 91
3"""