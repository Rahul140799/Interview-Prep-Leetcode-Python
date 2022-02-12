class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        start = word[0]
        
        def dfs(i,j,idx):
            if idx == len(word):
                return True
            
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[idx] or board[i][j] == '#':
                return False
            
            temp = board[i][j]
            board[i][j] = '#'
            
            res = dfs(i+1,j,idx+1) or dfs(i-1,j,idx+1) or dfs(i,j+1,idx+1) or dfs(i,j-1,idx+1)
            
            board[i][j] = temp
            
            return res
        
        flag = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == start:
                    ans = dfs(i,j,0)
                    if ans:
                        flag = 1
            
        if flag:
            return True
        
        return False
                