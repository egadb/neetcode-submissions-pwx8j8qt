# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
First thought:
put everything in a array
use two pointers to create new list
o(n)

So:
That means we can reverse the second half and merge the two halfs
Find mid point
Reverse second half
Merge

'''

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        prev = slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        first, second = head, prev
        while second:
            nxt1, nxt2 = first.next, second.next
            first.next = second
            second.next = nxt1
            first, second = nxt1, nxt2






