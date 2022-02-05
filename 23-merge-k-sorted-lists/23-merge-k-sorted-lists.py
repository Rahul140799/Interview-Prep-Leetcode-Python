import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:        
        res = []
        heapq.heapify(res)
        
        for i in lists:
            while i:
                heapq.heappush(res, i.val)
                i = i.next
        
        head = ListNode(None)
        final = head
        
        while res:
            head.next = ListNode(heapq.heappop(res))
            head = head.next
            
        return final.next
            
            
            