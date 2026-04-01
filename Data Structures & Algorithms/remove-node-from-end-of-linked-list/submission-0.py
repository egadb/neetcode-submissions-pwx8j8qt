# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
initial thought:
count to end, 
end - n = where we want 

go to that position
keep track of prev
point prev to next


bright way:
use two pointers
create a gap of n with right pointer
init left pointer at beginning
advance both pointers until right is at the end
tadam, remove left node
'''

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next
        return dummy.next

