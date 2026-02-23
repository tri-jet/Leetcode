class Solution:
    def binaryGap(self, n: int) -> int:
        maxGap = 0
        binStr = bin(n)[2:]
        startIndex = 0   # start will always be 1 as no leading zeroes included
        for x in range(1, len(binStr)):
            if binStr[x] == "1":
                if x-startIndex > maxGap:
                    maxGap = x-startIndex
                startIndex = x
        return maxGap
