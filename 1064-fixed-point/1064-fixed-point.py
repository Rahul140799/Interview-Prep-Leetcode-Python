class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        left = 0
        right = len(arr)-1
        
        while left < right:
            mid = (left + right)//2
            
            if arr[mid] >= mid:
                right = mid
            else:
                left = mid + 1
                
        return left if arr[left] == left else -1