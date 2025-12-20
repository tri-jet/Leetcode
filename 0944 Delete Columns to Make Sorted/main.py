class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # brute force basic version - how?
        # want to loop from i to len of str, and access each 
        if len(strs) == 1:
            return 0
        colCount = 0
        for x in range(len(strs[0])): # looping thru cols
            letterAbove = strs[0][x]
            for y in range(1,len(strs)): # looping thru each row to check if col not sorted
                if letterAbove > strs[y][x]:
                    colCount += 1
                    break
                else: letterAbove = strs[y][x]
        return colCount
