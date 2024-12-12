import heapq as hq
import math

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        for i in range(len(nums)):
            nums[i] *= -1
        
        heapq.heapify(nums)

        for i in range(k):
            current = heapq.heappop(nums)
            current *= -1
            score += current
            heapq.heappush(nums, math.ceil(current/3) * -1)
        
        return score
