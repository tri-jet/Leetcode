class Solution:
    def concatenatedBinary(self, n: int) -> int:
        concatStr = ""
        for x in range(1, n+1):
            concatStr += bin(x)[2:]
        return int(concatStr,2) % 1000000007
