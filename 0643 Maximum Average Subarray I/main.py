class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return float(nums[0])
        max = 0.0
        for x in range(0, len(nums)-k+1):
            if sum(nums[x:x+k])/k > max:
                max = sum(nums[x:x+k])/k
        return max
