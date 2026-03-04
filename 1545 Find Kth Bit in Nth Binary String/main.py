class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        return self.genString(n)[k-1]

    def genString(self, i: int) -> str:
        if i == 1:
            return "0"
        return self.genString(i-1) + "1" + self.invert(self.genString(i-1))[::-1]

    def invert(self, x: str) -> str:
        table = str.maketrans("01", "10")
        return x.translate(table)
