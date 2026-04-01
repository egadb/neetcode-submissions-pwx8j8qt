class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1       # tells us if there is a bit at that position
            res += (bit << (31 - i)) # if there is, add it to the res
        return res