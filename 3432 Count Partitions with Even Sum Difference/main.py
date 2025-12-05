class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count = 0
        lTotal = nums[0]
        rTotal = sum(nums[1:])
        for x in range(1, len(nums)):
            if (lTotal-rTotal) % 2 == 0:
                count += 1
            lTotal += nums[x]
            rTotal -= nums[x]
        return count
