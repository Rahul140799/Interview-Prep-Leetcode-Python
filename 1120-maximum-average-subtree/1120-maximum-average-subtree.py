# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.avg = -sys.maxsize
        
        def dfs(root, distance, curr):
            if not root:
                return curr,distance
            
            left,x = dfs(root.left, distance, curr)
            right,y = dfs(root.right, distance, curr)
            
            curr = left + right + root.val
            distance = x+y+1
            
            self.avg = max(self.avg, curr/distance)
            return curr, distance
        
        dfs(root, 0, 0)
        return self.avg