# implementing merge sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        # separate nums into recursively smaller sublists
        left = []
        right = []

        for i in range(len(nums)):
            if i < len(nums) / 2:
                left.append(nums[i])
            else: right.append(nums[i])

        # recursively sort both sublists + merge back together
        left = self.sortArray(left)
        right = self.sortArray(right)

        return self.merge(left, right)

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        # merge lists to form sorted list
        result = []

        # while both not empty
        while left and right:
            # if first left val is < right val, add to list and remove it from the list
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        
        #if one empty then just add remaining vals from non-empty list to result
        if left:
            result.extend(left)
        if right:
            result.extend(right)
        
        return result