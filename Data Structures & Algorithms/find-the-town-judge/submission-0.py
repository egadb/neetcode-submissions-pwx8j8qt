class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustedBy = defaultdict(int)
        trusts = defaultdict(int)

        for src, dst in trust:
            trusts[src] += 1
            trustedBy[dst] += 1


        for i in range(1,n+1):
            if trusts[i] == 0 and trustedBy[i] == n - 1:
                return i

        return -1