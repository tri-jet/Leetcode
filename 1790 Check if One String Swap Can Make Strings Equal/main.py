class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        wrongLetterCount = 0
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False

        for x in range(len(s1)):
            if s1[x] != s2[x]:
                wrongLetterCount += 1
                if wrongLetterCount > 2:
                    return False
        return True
