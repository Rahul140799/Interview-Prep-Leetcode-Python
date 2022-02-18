class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return str(0)
        
        stack = []
        for i in num:
            while stack and k and int(i) < int(stack[-1]):
                stack.pop()
                k -= 1
            stack.append(i)
        
        if k > 0:
            stack = stack[:-k]
            
        return str(int(''.join(stack)))