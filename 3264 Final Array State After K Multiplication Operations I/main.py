import heapq as hq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # a lil heap action. ascending order so pop first, multiply then re-add
        hq.heapify(nums)
        for _ in range(k):
            hq.heappush(nums, hq.heappop(nums)*multiplier)
        
        return list(nums)
