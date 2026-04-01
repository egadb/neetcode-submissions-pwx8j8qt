
'''
Brute force:
Could simply use a hashset but this would mean we are using extra space which the problem doesnt want

Better:
Hard to see but because of the range of the numbers, this is actually a linked list problem. Each indices points
to another one. If we have two nodes pointing to the same node, this means we have a cycle.
we also need to keep in mind we want to return the node that starts the cycle. the one that have 
two "parents".
'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        slow = 0

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]

            if fast == slow:
                break

        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow2 == slow:
                return slow
        


        return -1