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
            print(f"current before removing: {current}")
            current *= -1
            current -= math.floor(float(current)/2) 
            print(current)
            current *= -1
            
            hq.heappush(piles, current)
            # " remove floor(piles[i] / 2) stones from it." - defining part that I missed
        print(piles)
        piles = list(piles)
        for y in range(len(piles)):
            piles[y] *= -1

        return sum(piles)
        

