class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n == 1:
            return True
        binVersion = bin(n)[2:]
        for x in range(1, len(binVersion)):
            if binVersion[x-1] == binVersion[x]:
                return False
        return True
