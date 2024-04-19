class Node:
    def __init__(self,key,val,next=None,prev=None):
        self.key=key
        self.val=val
        self.next=next
        self.prev =prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left= Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self,node):
        prev, nxt = node.prev,node.next
        nxt.prev = prev
        prev.next = nxt
    
    def insert(self,node):
        prev,nxt = self.right.prev,self.right
        prev.next = nxt.prev = node
        node.next,node.prev = nxt,prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
