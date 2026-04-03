class ListNode:
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularQueue:
    def __init__(self, k: int):
        self.sizeLeft = k
        self.left = ListNode(0, None, None)
        self.right = ListNode(0, self.left, None)
        self.left.next = self.right

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        new = ListNode(value, self.right.prev, self.right)
        self.right.prev.next = new
        self.right.prev = new
        self.sizeLeft -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        newLast = self.left.next.next
        newLast.prev = self.left
        self.left.next = newLast
        self.sizeLeft += 1
        return True 

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.left.next.val
        
    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.right.prev.val

    def isEmpty(self) -> bool:
        return self.left.next == self.right

    def isFull(self) -> bool:
        return self.sizeLeft == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()