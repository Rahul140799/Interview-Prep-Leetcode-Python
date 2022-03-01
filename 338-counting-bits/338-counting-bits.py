class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0]*(n+1)
        arr[0] = 0
        
        for i in range(1,n+1):
            if i%2:
                arr[i] = arr[i-1] + 1
            else:
                arr[i] = arr[i//2]
        return arr
                
        