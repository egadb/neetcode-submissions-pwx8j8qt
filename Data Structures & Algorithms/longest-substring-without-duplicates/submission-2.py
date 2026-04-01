class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        win = set()
        L = 0
        res = 0

        for R in range(len(s)):
            while s[R] in win:
                win.remove(s[L])
                L += 1

            win.add(s[R])
            res = max(res, len(win))

        return res