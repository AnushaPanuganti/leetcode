def maxsumarr(nums):
    maxsum = nums[0]
    currentsum = nums[0]
    for num in nums[1:]:
        currentsum = max(num, currentsum + num)
        maxsum = max(maxsum, currentsum)

    return maxsum


print(maxsumarr([1, -2, 0, 5, -1, 2]))