"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy_old = {None:None}

        cur = head
        while cur:
            new = Node(cur.val)
            copy_old[cur] = new
            cur = cur.next
        
        cur = head
        while cur:
            new = copy_old[cur]
            new.next = copy_old[cur.next]
            new.random = copy_old[cur.random]
            cur = cur.next
        
        return copy_old[head]
