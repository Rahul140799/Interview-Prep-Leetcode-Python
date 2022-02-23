"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        
        queue = deque([node])
        d = {node: Node(node.val)}
        
        while queue:
            curr = queue.popleft()
            for i in curr.neighbors:
                if i not in d:
                    d[i] = Node(i.val)
                    queue.append(i)
                d[curr].neighbors.append(d[i])
        return d[node]
        
            