class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        column_number = 0
        l = len(columnTitle)
        
        for i in range(l):
            column_number += (ord(columnTitle[i])-64)*(26**(l-i-1))
        return column_number
            