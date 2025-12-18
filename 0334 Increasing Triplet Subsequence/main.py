class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        count = 1
        current = nums[0]
        for x in range(1,len(nums)):
            if x > current:
                count += 1
                if count == 3:
                    return True
                current = x

        return False
