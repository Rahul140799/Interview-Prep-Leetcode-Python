class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def compute_string(st, stack, it):
            
            while it < len(st):
                if stack and st[it] == '#':
                    stack.pop()
                else:
                    if st[it] != '#':
                        stack.append(st[it])
                it += 1
            # print(stack)
            return ''.join(stack)
        
        return compute_string(s, [], 0) == compute_string(t, [], 0)