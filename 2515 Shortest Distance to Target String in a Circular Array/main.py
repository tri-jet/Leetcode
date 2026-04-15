class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        # search for index of target, then just do the calc
        if words[startIndex] == target:
            return 0
        targetCount = words.count(target)
        if targetCount == 0:
            return -1
        
        # but assumes first occurrence is closest - but assuming no dupplicates?
        minDist = 101
        while(targetCount > 0):
            index = words.index(target)
            if min(abs(startIndex-index), len(words)-abs(startIndex-index)) < minDist:
                minDist = min(abs(startIndex-index), len(words)-abs(startIndex-index))
            words[index] = "*"
            targetCount -= 1
        return minDist
