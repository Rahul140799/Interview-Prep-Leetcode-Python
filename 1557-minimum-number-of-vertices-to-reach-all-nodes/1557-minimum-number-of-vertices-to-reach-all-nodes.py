class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0]*n
        
        for i in edges:
            indegree[i[1]] += 1
        # print(indegree)
        
        res = []
        for i,val in enumerate(indegree):
            if val == 0:
                res.append(i)
        return res