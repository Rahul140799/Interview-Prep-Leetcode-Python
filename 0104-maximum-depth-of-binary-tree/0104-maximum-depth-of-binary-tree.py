# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def recurse(root,depth):
            if not root:
                return depth
            
            l = recurse(root.left, depth+1)
            r = recurse(root.right, depth+1)
            
            return max(l,r)
            
        return recurse(root,0)