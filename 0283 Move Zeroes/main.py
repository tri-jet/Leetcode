class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        nonZeroCount = len(nums)
        x = 0 
        while x < nonZeroCount:
            if nums[x] == 0:
                nums.pop(x)
                nonZeroCount -= 1
                nums.append(0)
            else:
                x += 1
