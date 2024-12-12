import heapq as hq
import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(len(gifts)):
            gifts[i] *= -1
        
        heapq.heapify(gifts)

        for i in range(k):
            print(gifts)
            current = hq.heappop(gifts) * -1
            print(f"current: {current}")
            current = math.floor(math.sqrt(current))
            hq.heappush(gifts, current)
        
        return sum(gifts)
