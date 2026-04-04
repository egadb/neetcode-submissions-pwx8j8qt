class Solution:
    def minOperations(self, s: str) -> int:
        count = 0 # operations if s starts with 0

        for i, c in enumerate(s):
            if i % 2 == 0:
                count += 1 if c == '0' else 0
            else:
                count += 1 if c == '1' else 0

        return min(count, len(s) - count)
                