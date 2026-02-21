class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = bin(n)[2:]
        count = 0
        for x in bits:
            if x == "1":
                count += 1
        return count
