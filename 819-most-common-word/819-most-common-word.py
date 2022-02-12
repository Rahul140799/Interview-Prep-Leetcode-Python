class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        para = paragraph.lower()
        
        st = ''
        for char in para:
            if char.isalnum():
                st += char
            elif char == ' ':
                st += ' '
            elif char == ',':
                st += ' '
        
        not_allowed = set(banned)
        splitted_paragraph = st.split(' ')
        
        d = {}
        for i in splitted_paragraph:
            if i not in not_allowed and i.isalpha():
                if i not in d:
                    d[i] = 1
                else:
                    d[i] += 1
                    
        maxi = max(d.values())
        
        for i in d:
            if d[i] == maxi:
                return i
            