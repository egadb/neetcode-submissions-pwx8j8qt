
'''
just fill a minheap with (euqueueTime, processingTime, index)
create a list with only the index and return as response
'''

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        pending = []
        available = []
        heapq.heapify(pending)
        heapq.heapify(available)
        for i, t in enumerate(tasks):
            heapq.heappush(pending, (t[0], t[1], i))

        res = []
        time = 0
        while pending or available:
            while pending and pending[0][0] <= time:
                enquTime, procTime, i = heapq.heappop(pending)
                heapq.heappush(available, (procTime, i))

            if available:
                procTime, i = heapq.heappop(available)
                time += procTime
                res.append(i)
            else:
                time += 1


        return res
