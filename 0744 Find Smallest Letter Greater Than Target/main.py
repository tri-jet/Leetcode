class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # sorted so do we just do binary search?
        # brute force first - then optimise
        current = letters[0]
        if current > target:
            return current
        for x in range(1, len(letters)):
            if letters[x] > target and letters[x] > current:
                return letters[x]
            elif letters[x] > target and current > letters[x]:
                return current
        return current
