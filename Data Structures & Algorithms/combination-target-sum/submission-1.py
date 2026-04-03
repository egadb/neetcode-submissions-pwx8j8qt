class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        combination = []
        def dfs(i):
            if i == len(nums) or sum(combination) > target:
                return
            if sum(combination) == target:
                res.append(combination.copy())
                return

            combination.append(nums[i])
            dfs(i)
            
            combination.pop()
            dfs(i+1)
            
        dfs(0)
        return res