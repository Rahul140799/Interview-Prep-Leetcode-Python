import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        d = {}
        
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        heap = []
        heapq.heapify(heap)
        
        for i in d:
            heapq.heappush(heap, (-1*d[i], i))
            
        st = ""
        
        while heap:
            count1 = 0
            count2 = 0
            letter1 = ""
            letter2 = ""
            
            if heap:
                count1, letter1 = heapq.heappop(heap)
            if heap:
                count2, letter2 = heapq.heappop(heap)
            
            if st and letter1 == st[-1]:
                return ""
            
            if count1 < 0:
                st += letter1
                count1 += 1
                if count1 < 0:
                    heapq.heappush(heap, (count1, letter1))
            
            if count2 < 0:
                st += letter2
                count2 += 1
                if count2 < 0:
                    heapq.heappush(heap, (count2, letter2))
                
        return st