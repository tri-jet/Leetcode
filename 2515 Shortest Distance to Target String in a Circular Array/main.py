class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        # search for index of target, then just do the calc
        if words[startIndex] == target:
            return startIndex
        if words.count(target) == 0:
            return -1
        index = words.index(target)
        # but assumes first occurrence is closest - but assuming no dupplicates?

        if index < startIndex:
            return startIndex-index
        else: return (index-startIndex)
