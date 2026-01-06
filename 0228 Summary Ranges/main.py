import math
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        # basically ranges = consecutive lists
        ranges = []
        start = current = -math.inf
        for x in range(0, len(nums)):
            print(f"ranges: {ranges}, x: {x}, num = {nums[x]}")
            print(f"start: {start}, current: {current}")
            if start == -math.inf and current == -math.inf:
                start = nums[x]
                current = nums[x]
            elif nums[x] == current + 1:
                current = nums[x]
            else:
                if current == start:
                    ranges.append(str(int(start))) 
                else: ranges.append(str(int(start)) + "->" + str(int(current)))
                start = nums[x]
                current = nums[x]
        if current == start:
            ranges.append(str(int(start)))
        else: ranges.append(str(int(start)) + "->" + str(int(current)))
        return ranges
