# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newll = ListNode()
        nl = newll
        temp = list1
        pre = list2
        while temp and pre:
            if temp.val < pre.val:
                nl.next = temp
                temp = temp.next
            else:
                nl.next = pre
                pre = pre.next
            nl = nl.next
        if temp:
            while temp:
                nl.next = temp
                temp = temp.next
                nl = nl.next
        if pre:
            while pre:
                nl.next = pre
                pre = pre.next
                nl = nl.next
        nl = newll
        newll = nl.next
        return newll
        
            



        