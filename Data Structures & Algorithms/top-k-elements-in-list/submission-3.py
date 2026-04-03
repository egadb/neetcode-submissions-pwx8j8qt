class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums)+1)]
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1

        for n in count:
            print(n)
            print(bucket)
            bucket[count[n]].append(n)

        res = []

        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res


        return res