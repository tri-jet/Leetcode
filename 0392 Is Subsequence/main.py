class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False

        letters = list(s)
        print(letters)
        for letter in t:
            if letter == letters[0]:
                letters.pop(0)
                if len(letters) == 0:
                    return True
        return False
