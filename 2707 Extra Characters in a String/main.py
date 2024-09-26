class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        for word in dictionary:
            print(s)
            if s.find(word) != -1:
                print("found")
                s.replace(word,"")
        return len(s)