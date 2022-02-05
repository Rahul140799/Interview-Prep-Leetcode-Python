# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:        
        res = []
        for i in lists:
            while i:
                res.append(i.val)
                i = i.next
        res.sort()
        
        j = 0
        head = ListNode(None)
        final = head
        while j < len(res):
            head.next = ListNode(res[j])
            head = head.next
            j += 1
        return final.next
            
            
            