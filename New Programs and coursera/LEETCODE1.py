
def twoSum(nums, target):
    List2=[]
    for i in nums:
        for j in range(1, len(nums)):
            if (i + nums[j] == target):
                List2.append(nums.index(i))
                List2.append(nums.index(nums[j]))
    print(List2)

nums=[2,7,11,15]
target=9
twoSum(nums,target)