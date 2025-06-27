class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # hashMap + need all combs + need 0 
        # ooh not hashmap - two pointers if sorted + don't need indices
        nums.sort()
        triplets = []

        #[-1,0,1,2,-1,-4]
        #sorted: [-4, -1, -1, 0, 1 , 2]
        # so looping thru, maybe use binary search on right most values?
        # # start -4, then look at i+1, (left) and n (right) 
        # does -4, and -1 + 2 = 0 -> no
        # if total of L+R > positive of start -> Right--, if smaller -> left ++
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue    # if not first val, and num == previous, don't check
            
            left = i + 1
            right = len(nums) -1
            while(left < right):
                if nums[i] + nums[left] + nums[right] == 0:
                    triplets.append([nums[i],nums[left], nums[right]])
                    break
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else: left += 1
        return triplets 
