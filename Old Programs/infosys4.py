'''inp=list(map(int,input().split()))'''


# PF-Prac-4
def find_nine(nums):
    c = 0
    for i in range(len(nums)):
        if (nums[i] == 9 and c < 4):
            return True
        c += 1
    if c > 3:
        return False
    if (len(nums) < 4):
        for j in range(len(nums)):
            if (nums[j] == 9):
                return True
            else:
                return False


nums = [1, 9, 4, 5, 6]
print(find_nine(nums))

