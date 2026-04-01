class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums) #o(n)

        res = 0
        for n in nums_set:
            temp_res = 1
            while n-1 in nums_set:
                n -= 1
                temp_res += 1
            if temp_res > res:
                res = temp_res
        return res