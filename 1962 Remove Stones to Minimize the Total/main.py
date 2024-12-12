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
            print(piles)
            current = hq.heappop(piles)
            current *= -1
            current = math.floor(current/2) * -1
            
            hq.heappush(piles, current)
        
        piles = list(piles)
        for y in range(len(piles)):
            piles[i] *= -1

        return sum(piles)
