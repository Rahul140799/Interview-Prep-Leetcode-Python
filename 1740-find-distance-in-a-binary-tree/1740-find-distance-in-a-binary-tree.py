# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        def find_lca(root, p, q):
            if not root:
                return 
            
            if root.val == p or root.val == q:
                return root
            
            left = find_lca(root.left, p, q)
            right = find_lca(root.right, p, q)
            
            if left and right:
                return root
            else:
                return left or right
            
            
        lca = find_lca(root, p, q)
        # print(lca)
        
        def find_distance(node, lca, dist):
            if not lca:
                return 0
            
            if lca.val == node:
                return dist
            
            left = find_distance(node, lca.left, dist+1)
            right = find_distance(node, lca.right, dist+1)
            
            return left + right
        
        
        return find_distance(p, lca, 0) + find_distance(q, lca, 0)
        