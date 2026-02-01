class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # sort them? # 3 contiguous arrays - so just choose the lowest 3 ?
        # or have to be in that order
        # so first array always nums[0] - either as solo, or if next 2 are lower
        # so find next 2 smallest nums
        lowest = lowest2nd = float('inf')
        for x in range(1, len(nums)):
            if nums[x] < lowest:
                lowest2nd = lowest
                lowest = nums[x]
            elif nums[x] < lowest2nd:
                lowest2nd = nums[x]
        return nums[0] + lowest + lowest2nd
