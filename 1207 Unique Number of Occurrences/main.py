class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # use dict, count occurences of each number
        # convert ocurrences to set to remove dupes, compare dict to non-dupes set
        # if shorter, then some dupes existed
        numDict = {}
        for x in arr:
            numDict[x] = numDict.get(x,0) + 1
        
        return len(numDict) == len(set(numDict.values()))
