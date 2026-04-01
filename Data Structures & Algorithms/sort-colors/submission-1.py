class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0] * 3

        for color in nums:
            buckets[color] += 1
        
        curr = 0
        for i,b in enumerate(buckets):
            for j in range(b):
                nums[curr + j] = i
            curr += b

        

        