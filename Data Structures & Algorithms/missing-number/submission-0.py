class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        currSum = sum(nums)
        n = len(nums)
        targetSum = sum([i for i in range(n)])


        return targetSum - currSum + n