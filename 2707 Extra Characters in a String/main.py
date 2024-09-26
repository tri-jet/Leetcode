class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        for word in dictionary:
            print(s)
            if s.find(word) != -1:
                print("found")
                s = s.replace(word,"",1)
        return len(s)