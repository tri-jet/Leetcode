class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # brute force basic version - how?
        # want to loop from i to len of str, and access each 
        if len(strs) == 1:
            return 0
        colCount = 0
        for x in range(len(strs[0])):
            letterAbove = strs[0][x]
            for y in range(1,len(strs)-1):
                print(f"col index:{x}, strs index: {y} \n letterAbove: {letterAbove}, current: {strs[y][x]}")
                if letterAbove > strs[y][x]:
                    colCount += 1
                    break
                else: current = strs[y][x]
        return colCount
