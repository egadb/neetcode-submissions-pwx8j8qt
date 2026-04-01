class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        currSum = 0
        res = len(nums) + 1

        for R in range(len(nums)):
            currSum += nums[R]
            print(currSum)

            while currSum >= target:
                res = min(res, R-L+1)
                currSum -= nums[L]
                L += 1
                

        return 0 if res == len(nums) + 1 else res

            