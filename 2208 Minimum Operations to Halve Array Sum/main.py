import heapq
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        opCount = 0
        arrSum = sum(nums)
        target = arrSum/2
        arrHeap = []
        # sort the numbers from high to low (heap?)
        # halve the greatest number, subtract the half from the arrSum to calc newSum
        # while arrSum < target

        # need largest val -> multiplying each value by -1 to apply to smallest val
        for x in nums:
            heapq.heappush(arrHeap,-x)
        
        while(arrSum > target):
            print(arrSum)
            current = heapq.heappop(arrHeap) * -1
            current /= 2
            arrSum -= current
            heapq.heappush(arrHeap, -current)
            opCount += 1

        return opCount
