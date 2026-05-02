'''
is there always a majority
how big is the data
are the elements always numbers can they be superbig


first idea:
make a hashset/counter and just return the biggest
but ideally we need constant space
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)

        res = 0
        majority = 0
        for k, v in counter.items():
            if majority < v:
                majority = v
                res = k

        return res