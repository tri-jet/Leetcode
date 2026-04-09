class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # leftmost so just best to go left to right from the start
        # also not including middle.
        if len(nums) == 1:
                return 0
        if len(nums) == 2:
            if nums[0] == 0:
                return 1
            if nums[1] == 0:
                return 0
        
        leftSum = 0
        rightSum = sum(nums[1:])
        middle = 0
        if leftSum == rightSum:
            return middle
        while(middle < len(nums)-1):
            middle += 1
            leftSum += nums[middle-1]
            rightSum -= nums[middle]
            if rightSum == leftSum:
                return middle
        if rightSum != leftSum:
            return -1
