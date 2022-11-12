from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        
        for i in strs:
            arr = [0]*26
            for j in i:
                arr[ord(j)-97] += 1
            
            st = ""
            for idx,val in enumerate(arr):
                if val:
                    st += chr(idx+97)*val
            d[st].append(i)
            
        return d.values()
            