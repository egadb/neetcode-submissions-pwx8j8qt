'''

'''
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n+1)

        def recure(i: int) -> int:
            if i <= 3:
                return i
            if memo[i] != -1:
                return memo[i]
            memo[i] = recure(i-1) + recure(i-2)
            return memo[i]

        return recure(n)