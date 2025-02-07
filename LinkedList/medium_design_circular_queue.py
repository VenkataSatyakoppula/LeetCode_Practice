class ListNode:
    def __init__(self,val,prev = None,nxt = None):
        self.prev , self.next , self.val= prev,nxt,val

class MyCircularQueue:
    def __init__(self, k: int):
        self.n = k
        self.left = ListNode(-1,None,None)
        self.right = ListNode(-1,self.left,None)
        self.left.next = self.right

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        cur = ListNode(value,self.right.prev,self.right)
        self.right.prev.next = cur
        self.right.prev = cur
        self.n -= 1
        return True
        
    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.n +=1
        return True

    def Front(self) -> int:
        return self.left.next.val

    def Rear(self) -> int:
        return self.right.prev.val

    def isEmpty(self) -> bool:
        return self.left.next == self.right

    def isFull(self) -> bool:
        return self.n == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
