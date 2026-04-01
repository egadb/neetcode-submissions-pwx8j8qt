class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isEatingRateValid(k: int) -> bool:
            hoursTaken = 0
            for p in piles:
                hoursTaken += math.ceil(p / k)
            return hoursTaken <= h

        l, r = 1, max(piles)

        while l < r:
            m = (r+l) // 2

            if isEatingRateValid(m):
                r = m
            elif not isEatingRateValid(m):
                l = m + 1
        
        return l
