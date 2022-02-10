# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.paths = 0
        
        def compute(root, target):
            if not root:
                return
            
            if target == root.val:
                self.paths += 1
                
            compute(root.left, target-root.val)
            compute(root.right, target-root.val)
        
        def dfs(root, target):
            if not root:
                return
            
            compute(root, target)
            dfs(root.left, target)
            dfs(root.right, target)
        
        dfs(root, targetSum)
        return self.paths