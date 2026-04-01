class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        L, R = 0, len(nums) - 1

        while L <= R:
            if nums[L] < nums[R]:
                res = min(res, nums[L])
                break

            mid = (L + R) // 2 
            res = min(res, nums[mid])
            if nums[L] > nums[mid]:
                R = mid - 1
            else:
                L = mid + 1

        return res
