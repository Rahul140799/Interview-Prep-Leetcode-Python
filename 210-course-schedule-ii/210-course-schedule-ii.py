from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0]*numCourses
        
        queue = deque([])
        res = []
        
        for i in prerequisites:
            graph[i[1]].append(i[0])
            indegree[i[0]] += 1
        
        for i,val in enumerate(indegree):
            if not val:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            res.append(node)
            
            if node in graph:
                for val in graph[node]:
                    indegree[val] -= 1

                    if not indegree[val]:
                        queue.append(val)
                
        return res if len(res) == numCourses else []
        