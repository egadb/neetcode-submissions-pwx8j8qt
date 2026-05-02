
'''
calculate min cost from the end to the first return min between 0 and 1
'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost) - 1, -1, -1):
            if i < len(cost)-2:
                cost[i] = cost[i] + min(cost[i+1], cost[i+2])

        return min(cost[0], cost[1])
