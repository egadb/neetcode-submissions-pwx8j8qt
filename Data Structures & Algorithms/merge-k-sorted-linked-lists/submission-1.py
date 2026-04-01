# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        interval = 1
        while interval < len(lists):
            # Merge pairs: (0,1), (2,3), (4,5)... then (0,2), (4,6)...
            for i in range(0, len(lists) - interval, interval * 2):
                lists[i] = self.mergeLists(lists[i], lists[i + interval])
        
            # Double the interval to jump over already merged lists
            interval *= 2
        return lists[0]

    def mergeLists(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next
