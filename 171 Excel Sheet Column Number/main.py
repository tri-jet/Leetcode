class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alphabet = { chr(ord('A') + i): i+1 for i in range(0,26) } # 1 line dictionary init
        colNum = 0
        for i in range(len(columnTitle)):
            colNum += (26^(len(columnTitle) - i-1)) * alphabet.get(columnTitle[i]) 
        return colNum
