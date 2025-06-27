class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Loop through nums, do binary search and using the left and right pointers to find the pair that combines with the starting value to make 0.
        # Keep moving through nums if multiple solutions for start value, and ensuring move past any duplicate start values 
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue    # if not first val, and num == previous, don't check
            
            left = i + 1
            right = len(nums) -1
            while(left < right):
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left +=1 
                elif total > 0:
                    right -= 1
                else:
                    triplets.append([nums[i],nums[left], nums[right]])
                    left+= 1
                    while(nums[left] == nums[left-1] and left < right):
                        left+= 1
        return triplets 
