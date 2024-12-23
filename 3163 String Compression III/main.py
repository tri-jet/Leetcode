class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        current = word[0]
        currentCount = 1
        for i in range(1,len(word)):
            if word[i] == current:
                currentCount += 1
                if currentCount > 9:
                    comp = comp + str(currentCount-1) + str(current)
                    currentCount = 1
            else: # word[i] != current
                comp = comp + str(currentCount) + str(current)
                current = word[i]
                currentCount = 1
        comp = comp + str(currentCount) + str(current)
        return comp
