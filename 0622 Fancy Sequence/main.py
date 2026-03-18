class Fancy:
    fancySeq = []
    def __init__(self):
        fancySeq = []

    def append(self, val: int) -> None:
        self.fancySeq.append(val)

    def addAll(self, inc: int) -> None:
        for x in range(0,len(self.fancySeq)):
            self.fancySeq[x] += inc

    def multAll(self, m: int) -> None:
        for x in range(0,len(self.fancySeq)):
            self.fancySeq[x] *= m
        

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.fancySeq):
            return -1
        return self.fancySeq[idx] % (10**9 + 7)


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
