# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or (len(lists) == 0):
            return None
        
        while(len(lists) > 1):
            t = []
            for i in range(0,len(lists),2):
                A = lists[i]
                B = lists[i+1] if(i+1)<len(lists) else None
                t.append(self.mergelist(A,B))
            lists = t
        return lists[0]
    
    def mergelist(self,l1,l2):
        #todo
        dummy = ListNode()
        tail = dummy

        while(l1 and l2):
            if(l1.val < l2.val):
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        if(l1):
            tail.next = l1
        if(l2):
            tail.next = l2
        
        return dummy.next

