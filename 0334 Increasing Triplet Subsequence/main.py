class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # find num smaller than infinity
        # if x is not smaller than x1 but is less than x2 - then it means x1 < x < infinity
        # that means if the next value is less than x1, still know we had a valid x1, x2 sequence
        # if next value is greater than x1 but less than x2, then still got a valid x1 and new x2 sequence
        # then if value greater than x2 and x2 - makes it a valid triplet sequence
        x1 = float('inf')
        x2 = float('inf')
        for x in nums:
            if x <= x1:
                x1 = x
            elif x <= x2:
                x2 = x
            else:
                return True
        return False
