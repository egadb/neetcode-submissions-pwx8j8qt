class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        visit = set()
        def dfs(curr, par):
            if curr in visit:
                return True

            visit.add(curr)
            for nei in adj[curr]:
                if nei != par and dfs(nei, curr):
                    return True
            return False

        for a, b in edges:
            visit = set()
            adj[a].append(b)
            adj[b].append(a)

            if dfs(a, -1):
                return [a, b]

        return []
