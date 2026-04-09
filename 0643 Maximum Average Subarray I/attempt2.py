class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        startSum = sum(nums[0:k])
        avg = startSum / k
        for x in range(0,len(nums)-k):
            # sliding window, so drop first, and add new end
            #startSum = nums[0+x:x+k]
            startSum -= nums[x] # remove start
            startSum += nums[k+x]
            if startSum/k > avg:
                avg = startSum/k
        return avg
