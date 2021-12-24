class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        l = 0
        
        for i in range(1,len(arr)-1):
            
            j = i-1
            k = i+1
            
            if j >= 0 and arr[j] < arr[i] > arr[k] and k < len(arr):
                while j-1 >= 0 and arr[j] > arr[j-1]:
                    j -= 1
                while k+1 < len(arr) and arr[k] > arr[k+1]:
                    k += 1           
                l = max(l, k-j+1)
        return l
                