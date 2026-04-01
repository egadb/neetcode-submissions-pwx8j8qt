# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        total = []
        for l in lists:
            while l:
                total.append(l.val)
                l = l.next
        total.sort()

        res = ListNode()
        cur = res
        for i in total:
            cur.next = ListNode(i)
            cur = cur.next
        return res.next