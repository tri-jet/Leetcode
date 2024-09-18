class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums.remove(min(nums))
        nums.remove(max(nums))
        if not nums:
            return -1
        else: return nums[0]
