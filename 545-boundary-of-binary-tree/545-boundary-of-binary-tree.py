# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        arr = [root.val]
        visited = set()
        visited.add(root)
        
        def left_border(root):
            if not root:
                return
            
            arr.append(root.val)
            visited.add(root)
            
            if root.left:
                left_border(root.left)
            else:
                left_border(root.right)
        
        left_border(root.left)
        
        def leaves(root):
            if not root:
                return 
            
            leaves(root.left)
            leaves(root.right)
            
            if(not root.left and not root.right and root not in visited):
                arr.append(root.val)
                visited.add(root)
        
        leaves(root)
        
        def right_border(root):
            if not root:
                return
            
            if root.right:
                right_border(root.right)
            else:
                right_border(root.left)
                
            if root not in visited:
                arr.append(root.val)
                visited.add(root)
                
        right_border(root.right)
        
        return arr
    
    