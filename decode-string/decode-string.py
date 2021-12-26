class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            stack.append(i)
            
            temp = ""
            flag = 0
            while stack and i == ']' and stack[-1] != '[':
                temp += stack.pop()
                flag = 1
            
            if flag == 1:
                stack.pop()
                
                n = ""
                while stack and stack[-1].isnumeric():
                    n += stack.pop()
                num = int(n[::-1])
                temp *= num

                for j in temp[::-1]:
                    if j != ']':
                        stack.append(j)
        
        return ''.join(stack)