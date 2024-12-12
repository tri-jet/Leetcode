import heapq as hq
import math

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # half stones to create smallest possible vals -> choose largest one each time
        # basically same as 2558?
        for i in range(len(piles)):
            piles[i] *= -1
        hq.heapify(piles)
        for x in range(k):
            current = hq.heappop(piles)
            current *= -1
            current -= math.floor(float(current)/2)  # " remove floor(piles[i] / 2) stones from it." - defining part that I missed
            current *= -1
            
            hq.heappush(piles, current)
            
        piles = list(piles)
        for y in range(len(piles)):
            piles[y] *= -1

        return sum(piles)
        

