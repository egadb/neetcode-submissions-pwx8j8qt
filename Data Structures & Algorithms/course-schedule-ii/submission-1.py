class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = defaultdict(int)
        adj = [[] for i in range(numCourses)]

        for pre in prerequisites:
            indegree[pre[0]] += 1 
            adj[pre[1]].append(pre[0])

        res = []
        def dfs(curr):
            res.append(curr)
            indegree[curr] -= 1
            for child in adj[curr]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    dfs(child)

            
        for i in range(numCourses):
            if indegree[i] == 0:
                dfs(i)
        print(res)
        return res if len(res) == numCourses else []
