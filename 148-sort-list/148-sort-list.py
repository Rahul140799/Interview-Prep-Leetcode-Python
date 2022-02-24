# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        
        while head:
            arr.append(head.val)
            head = head.next
        
        arr.sort()
        
        first = ListNode(-1)
        second = first
        
        for i in arr:
            second.next = ListNode(i)
            second = second.next
            
        return first.next
            
        