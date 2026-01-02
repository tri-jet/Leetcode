class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        numDict = {}
        for x in nums:
            numDict[x] = numDict.get(x,0) + 1
            if numDict[x] == len(nums)/2:
                return x
