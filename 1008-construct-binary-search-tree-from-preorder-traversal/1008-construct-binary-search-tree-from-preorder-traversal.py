# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inorder = sorted(preorder)
        
        def construct_tree(inorder, preorder):
            if not inorder or not preorder:
                return 
            
            root = TreeNode(preorder[0]) 
            idx = inorder.index(preorder[0])
            
            root.left = construct_tree(inorder[:idx], preorder[1:idx+1])
            root.right = construct_tree(inorder[idx+1:], preorder[idx+1:])
            
            return root
        
        return construct_tree(inorder, preorder)
    