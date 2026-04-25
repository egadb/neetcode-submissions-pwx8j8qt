class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [(-cnt, val) for val, cnt in Counter(tasks).items()]
        heapq.heapify(heap)

        time = 0
        q = deque()
        while heap or q:
            time += 1
            if heap:
                (cnt, val) = heapq.heappop(heap)
                cnt = cnt + 1
                if cnt:
                    q.append([(cnt, val), time + n])

            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        return time