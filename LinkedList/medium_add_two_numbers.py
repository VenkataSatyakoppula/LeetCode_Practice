# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = l1, l2
        carry = 0
        prev = None
        head = None
        while cur1 or cur2:
            if cur1 and cur2:
                value = cur1.val+cur2.val+carry
            elif cur1 and not cur2:
                value = cur1.val+carry
            elif not cur1 and cur2:
                value = cur2.val+carry
            carry=0
            if value>=10:    
                value = value%10
                carry=1
            if prev:
                new = ListNode(value)
                prev.next = new
                prev = new
            else:
                head = ListNode(value)
                prev = head
            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
        if carry==1:
            new = ListNode(carry)
            prev.next = new
        return head
