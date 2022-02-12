from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque([(beginWord, 0)])
        
        visited = set()
        visited.add(beginWord)
        
        destination = set(wordList)
        
        while queue:
            word, distance = queue.popleft()
            
            if word == endWord:
                return distance + 1
            
            for i in range(len(word)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i]+j+word[i+1:]
                    
                    if new_word in destination and new_word not in visited:
                        queue.append((new_word, distance+1))
                        visited.add(new_word)
        return 0
            