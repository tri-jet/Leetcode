class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        stage = 0   # stage 1 - increasing, 2 - decreasing, 3 increasing
        for x in range(1, len(nums)):
            if nums[x-1] < nums[x]:
                if stage == 0:
                    if x >= 1:
                        stage += 1
                    else: return False # if first 2 didn't trigger increasing, then won't work
                elif stage == 1:
                    continue
                elif stage == 2:
                    stage += 1
                elif stage == 3:
                    continue
            elif nums[x-1] > nums[x]:
                if stage == 0:
                    return False # if goes 2,1,3 - can't start decreasing at stage 0
                elif stage == 1:
                    stage += 1
                elif stage == 2:
                    continue
                elif stage == 3:
                    return False # if increasing again, can't decrease again
            # strictly increasing/decreasing, so no duplicate contiguous nums
            else: return False
        return stage == 3
