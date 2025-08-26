class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        for x in words2:
            for y in words1:
                if x not in y:
                    words1.remove(y)
                    continue
        return words1
