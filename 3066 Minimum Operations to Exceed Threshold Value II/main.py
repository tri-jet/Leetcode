import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # only need heap and then pop twice to x,y
        # while the heap's lowest value < k, keep going
        opCount = 0
        heapq.heapify(nums)
        while(nums[0] < k):
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, min(x,y)*2 + max(x,y))
            opCount += 1
        return opCount
