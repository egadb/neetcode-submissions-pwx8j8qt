
'''
brute force:
for each subaray calculate the sum.
    if sum == k:
        increment res

Better:
I can do a prefixsum array but i still need to go through each subarray so it doesnt actually save time
However we can store the prefixsum in some hashset and from there check in constant time if there is
a prefix that is equal to currsum - prefix = k for every
if so, increment res

'''



class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSumCount = {0:1}
        res = 0
        curSum = 0

        for n in nums:
            curSum += n
            diff = curSum - k
            res += preSumCount.get(diff, 0)
            if curSum not in preSumCount:
                preSumCount[curSum] = 1 
            else:
                preSumCount[curSum] += 1

        return res