# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def recurse(root, count):
            if not root:
                return 0
            
            left = 0
            right = 0
            
            left = recurse(root.left, count+1)
            right = recurse(root.right, count+1)
            
            return left + right + 1
        
        return recurse(root, 0)