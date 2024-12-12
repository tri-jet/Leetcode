import heapq as hq
import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(len(gifts)):
            gifts[i] *= -1
        
        heapq.heapify(gifts)

        for i in range(k):
            current = hq.heappop(gifts) * -1
            current = math.floor(math.sqrt(current))
            hq.heappush(gifts, -current)

        gifts = list(gifts)
        for i in range(len(gifts)):
            gifts[i] *= -1
        
        return sum(gifts)
