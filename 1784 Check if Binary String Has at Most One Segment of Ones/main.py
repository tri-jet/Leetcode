class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if len(s) == 0:
            return s[x] == 1
        # if starts with 1, or 0 but no other
        for x in range(1, len(s)):
            if s[x] == "1" and s[x-1] == "0":
                return False
        return s[0] == "1"
