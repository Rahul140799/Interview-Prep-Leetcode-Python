class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def check(arr, target):
            left = 0
            right = len(arr)
            
            while left < right:
                mid = (left + right)//2
                if arr[mid] == target:
                    return True
                elif arr[mid] > target:
                    right = mid
                else:
                    left = mid + 1
            return False
                
        for i in matrix:
            if check(i, target):
                return True
        return False