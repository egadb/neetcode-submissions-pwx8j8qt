class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        L = 0
        win = set()

        for R in range(len(nums)):
            if R - L > k:
                win.remove(nums[L])
                L += 1

            if nums[R] in win:
                return True
            win.add(nums[R])

        return False