# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:        
        
        def is_valid(root, temp):
            if not root:
                return False
            
            temp.append(root.val)            
            left = is_valid(root.left, temp)
            right = is_valid(root.right, temp)
            
            if temp == arr and not root.left and not root.right:
                return True
            
            temp.pop()
            
            return left or right
        
        return is_valid(root, [])