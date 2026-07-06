# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        if head.next == None:
            return False
        pre = head
        post = head.next.next
        while post:
            if post.next == None:
                return False
            post = post.next.next
            pre = pre.next
            if pre == post:
                return True
        return False