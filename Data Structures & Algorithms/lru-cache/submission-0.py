class ListNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prv = None
        self.nxt = None

class LRUCache:
    def __init__(self, capacity: int):
        self.front, self.back = ListNode(0, 0), ListNode(0, 0)
        self.front.nxt, self.back.prv = self.back, self.front
        self.cap = capacity
        self.cache = {}

    def remove(self, node):
        prv, nxt = node.prv, node.nxt
        prv.nxt, nxt.prv = nxt, prv

    def insert(self, node):
        prv, nxt = self.back.prv, self.back
        prv.nxt = nxt.prv = node
        node.nxt, node.prv = nxt, prv

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])

        if self.cap < len(self.cache):
            lru = self.front.nxt
            self.remove(lru)
            del self.cache[lru.key]
