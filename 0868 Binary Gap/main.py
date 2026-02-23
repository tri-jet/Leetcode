class Solution:
    def binaryGap(self, n: int) -> int:
        maxGap = 0
        binStr = bin(n)[2:]
        startIndex = 0   # start will always be 1 as no leading zeroes included
        currentGap = 0  # do I need this if I have start and end index? probs not
        for x in range(1, len(binStr)):
            if binStr[x] == "1":
                currentGap = x-startIndex
                if currentGap > maxGap:
                    maxGap = currentGap
                startIndex = x
                currentGap = 0
        return maxGap
