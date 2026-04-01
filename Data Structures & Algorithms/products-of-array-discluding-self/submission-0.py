class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix = [0]*len(nums)
        prefix = [0]*len(nums)
        res = [0]*len(nums)
        m = 1

        for i, n in enumerate(nums):
            m *= n
            prefix[i] = m

        m = 1
        length = len(nums)
        for i, n in enumerate(reversed(nums)):
            m *= n
            suffix[length - 1 - i] = m

        for i, n in enumerate(nums):
            if i == 0:
                res[i] = suffix[i+1]
            elif i == len(nums) - 1:
                res[i] = prefix[i-1]
            else:
                res[i] = prefix[i-1] * suffix[i+1]


        return res