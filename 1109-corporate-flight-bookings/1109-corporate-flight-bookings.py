class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        arr = [0] * (n+1)
        
        for i in bookings:
            start = i[0]-1
            end = i[1]
            amount = i[2]
            
            arr[start] += amount
            arr[end] -= amount
            
        for i in range(1,len(arr)):
            arr[i] += arr[i-1]
        return arr[:-1]