class Solution:
    def compute_string(self, st: str, stack: list, it: int) -> list:
            while it < len(st):
                if stack and st[it] == '#':
                    stack.pop()
                else:
                    if st[it] != '#':
                        stack.append(st[it])
                it += 1
            return ''.join(stack)
        
    def backspaceCompare(self, s: str, t: str) -> bool:          
        return self.compute_string(s, [], 0) == self.compute_string(t, [], 0)