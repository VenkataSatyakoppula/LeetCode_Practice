class ListNode:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
class MyHashSet:

    def __init__(self):
        self.map = [ListNode(0) for i in range(10**4)]

    def add(self, key: int) -> None:
        cur = self.map[key%10**4]
        while cur.next:
            if cur.next.val == key:
                return
            cur = cur.next
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        cur = self.map[key%10**4]
        while cur.next:
            if cur.next.val == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        cur = self.map[key%10**4]
        while cur.next:
            if cur.next.val == key:
                return True
            cur = cur.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
