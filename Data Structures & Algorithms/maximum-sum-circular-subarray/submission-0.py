class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMax = 0
        currMin = 0
        globalMax = nums[0]
        globalMin = nums[0]
        total = 0

        for n in nums:
            currMax = max(n, currMax + n)
            currMin = min(n, currMin + n)
            total += n
            globalMax = max(currMax, globalMax)
            globalMin = min(currMin, globalMin)


        return max(globalMax, total - globalMin) if globalMax > 0 else globalMax
            