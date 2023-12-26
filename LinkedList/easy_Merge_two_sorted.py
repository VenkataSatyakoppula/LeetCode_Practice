# Definition for singly-linked list.
 class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
def mergeTwoLists(self, list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    if not list1 and  not list2:
        return None
    elif not list1:
        return list2
    elif not list2:
        return list1
    else:
        h1 = list1
        h2 = list2
        res = ListNode()
        temp = res
        while h1 and h2:
            if (h1.val <= h2.val):
                temp.next = h1
                h1 = h1.next
            elif(h1.val > h2.val):
                temp.next = h2
                h2 = h2.next
            temp = temp.next
        if not h1:
            temp.next = h2
        if not h2:
            temp.next = h1
        return res.next
