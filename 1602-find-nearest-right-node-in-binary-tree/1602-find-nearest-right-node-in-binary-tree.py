# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        if not root:
            return None
        
        queue = deque([root])
        flag = 0
        
        while queue:
            l = len(queue)
            temp = []
            while l:
                curr = queue.popleft()
                temp.append(curr.val)

                if flag == 1 and len(temp) > 1:
                    return curr

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

                if curr and curr == u and len(temp) >= 1:
                    flag = 1
                else:
                    flag = 0
                
                l -= 1
            
        return None
            
            