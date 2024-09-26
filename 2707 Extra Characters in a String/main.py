class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        for word in dictionary:
            if s.find(word) != -1:
                s.replace(word,"")
        return len(s)