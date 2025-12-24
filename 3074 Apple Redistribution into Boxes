class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
       totalApples = sum(apple)
       capacity.sort()
       boxCount = 0
       for x in range(len(capacity)-1, -1, -1):
        if totalApples == 0:
            return boxCount
        if capacity[x] <= totalApples:
            boxCount += 1
            totalApples -= capacity[x]
       return boxCount 
