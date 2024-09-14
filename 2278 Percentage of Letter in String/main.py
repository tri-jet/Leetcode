class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        if letter not in s:
            return 0
        count = 0
        for x in s:
            if x == letter:
                count += 1
        return int(count*100/len(s))