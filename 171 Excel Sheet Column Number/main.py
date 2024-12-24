class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alphabet = { chr(ord('A') + i): i+1 for i in range(0,26) } # 1 line dictionary init
        colNum = 0
        for char in columnTitle:
            colNum += alphabet.get(char)
        return colNum
