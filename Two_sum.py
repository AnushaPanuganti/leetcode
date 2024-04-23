def twosum(nums, target):
    numtoindex = {}
    for i in range(len(nums)):
        if target - nums[i] in numtoindex:
            return [numtoindex[target - nums[i]] , i]
        numtoindex[nums[i]] = i
    return []
    
print(twosum(nums = [3,3,4,5], target = 9))
