class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        l1 = version1.split('.')
        l2 = version2.split('.')
        
        if len(l1) < len(l2):
            for i in range(len(l2)-len(l1)):
                l1.append('0')
        elif len(l2) < len(l1):
            for i in range(len(l1)-len(l2)):
                l2.append('0')
        
        li = list(zip(l1,l2))
        
        for i in range(len(li)):
            n1 = li[i][0]
            n2 = li[i][1]
            
            if int(n1) < int(n2):
                return -1
            elif int(n1) > int(n2):
                return 1
            
        return 0
                