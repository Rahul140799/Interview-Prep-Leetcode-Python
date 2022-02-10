# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        def dfs(root, nodes):
            if not root:
                return None
            
            for i in nodes:
                flag = 0
                if root != i:
                    flag = 1
                
                if not flag:
                    return root
            
            l = dfs(root.left, nodes)
            r = dfs(root.right, nodes)
            
            if l and r:
                return root
            else:
                return l or r
        
        return dfs(root, nodes)