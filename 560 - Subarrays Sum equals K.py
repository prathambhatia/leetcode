from collections import defaultdict
def subarraySum(nums,k):

    prevSum = defaultdict(int)
    prevSum[0] = 1
    res = 0
    total = 0
    
    for r in range(len(nums)):
        total += nums[r]
        
        rem = total - k
        if rem in prevSum:
            res += prevSum[rem]
        prevSum[total] += 1
    return print('Total number of subarrays are:' ,res) 

nums = [1,2,3,-3,1,1,1,4,2,-3]
k = 3
subarraySum(nums, k)
