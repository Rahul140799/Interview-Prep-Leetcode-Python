class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        opening = set()
        opening.add('[')
        opening.add('(')
        opening.add('{')
        
        for i in s:
            if i in opening:
                stack.append(i)
            else:
                if stack and i == ')' and stack[-1] == '(':
                    stack.pop()
                elif stack and i == ']' and stack[-1] == '[':
                    stack.pop()
                elif stack and i == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(i)
                    
        return not len(stack)
                    