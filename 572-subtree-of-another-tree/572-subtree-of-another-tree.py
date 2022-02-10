# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def is_same(root, sub):
            if not root and not sub:
                return True
            
            if not root or not sub:
                return False
            
            if root.val == sub.val:
                return is_same(root.left, sub.left) and is_same(root.right, sub.right)
        
        def dfs(root, sub):
            if not root:
                return False
            
            if root.val == sub.val and is_same(root, sub):
                return True
            
            return dfs(root.left, sub) or dfs(root.right, sub)
        
        
        return dfs(root, subRoot)