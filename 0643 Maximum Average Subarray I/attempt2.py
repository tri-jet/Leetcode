class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        startSum = sum(nums[0:k])
        avg = startSum / k
        for x in range(1,len(nums)-k):
            # sliding window, so drop first, and add new end
            #startSum = nums[0+x:x+k]
            startSum -= nums[x-1] # remove start
            startSum += nums[k+x-1]
            if startSum/k > avg:
                avg = startSum/k
        return avg
