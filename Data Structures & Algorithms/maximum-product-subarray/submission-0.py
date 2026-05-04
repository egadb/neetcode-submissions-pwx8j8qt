'''
could be done with prefix suffix or kadanes algorithm
hard to see thats its actually a dp problem
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1, 1
        res = nums[0]

        for n in nums:
            tmp = curMax * n
            curMax = max(n*curMax, curMin*n, n)
            curMin = min(tmp, curMin*n, n)
            res = max(curMax, res)

        return res