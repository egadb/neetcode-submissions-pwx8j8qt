'''
sort,
go through each intervals in a loop
two cases:
1. interval overlaps with previous, merge and add to res
2. interval is strictly greater, add to res
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        res = [intervals[0]]

        for (start, end) in intervals:
            lastStart = res[-1][0]
            lastEnd = res[-1][1]
            if lastEnd >= start:
                res[-1] = [min(lastStart, start), max(lastEnd, end)]
            else:
                res.append([start,end])

        return res