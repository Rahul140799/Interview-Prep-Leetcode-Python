class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1], reverse=True)
        print(boxTypes)
        
        if truckSize < boxTypes[0][0]:
            return truckSize * boxTypes[0][1]
        
        i = 0
        count = 0
        
        weight = 0
        
        while i < len(boxTypes):
            if count + boxTypes[i][0] <= truckSize:
                weight += boxTypes[i][0] * boxTypes[i][1]
                count += boxTypes[i][0]
                i += 1
            else:
                break
        
        if i < len(boxTypes) and count <= truckSize:
            weight += (truckSize-count)*boxTypes[i][1]
        return weight
                
        