class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        nums.remove(min(nums))
        nums.remove(max(nums))
        return nums[0]
