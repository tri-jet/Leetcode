class Fancy:
    fancySeq = []
    changes = []
    def __init__(self):
        self.fancySeq.clear()
        self.changes.clear()

    def append(self, val: int) -> None:
        self.fancySeq.append(val)

    def addAll(self, inc: int) -> None:
        self.changes.append(f"+{inc}")

    def multAll(self, m: int) -> None:
        self.changes.append(f"*{m}")
        

    def getIndex(self, idx: int) -> int:
        print(self.fancySeq)
        print(self.changes)
        if idx >= len(self.fancySeq):
            return -1
        value = self.fancySeq[idx]
        for op in self.changes:
            if op[0] == "+":
                value += int(op[1:])
            elif op[0] == "*":
                value *= int(op[1:])
        return value % (10**9 + 7)


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
