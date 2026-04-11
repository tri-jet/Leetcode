class RecentCounter:
    q = []
    def __init__(self):
        self.q = []

    def ping(self, t: int) -> int:
        self.q.append(t)
        count = 0
        for x in self.q:
            if x >= t-3000:
                count += 1
        return count        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
