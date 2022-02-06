class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x:x[1])
        # print(trips)
        
        arr = [0]*1001
        
        for i in trips:
            arr[i[1]] += i[0]
            arr[i[2]] -= i[0]
        # print(arr)
        
        if arr[0] > capacity:
            return False
        
        for i in range(1,len(arr)):
            if arr[i] + arr[i-1] > capacity:
                return False
            else:
                arr[i] += arr[i-1]
        # print(arr)
        return True
    