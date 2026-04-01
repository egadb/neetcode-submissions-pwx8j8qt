class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for i, r in enumerate(s):
            while r in charSet:
                charSet.remove(s[l])
                l += 1

            charSet.add(r)
            res = max(res, i - l + 1)

        return res