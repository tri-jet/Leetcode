class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # same principles as 643 
        # count num of vowels in initial subtring
        # loop from  0, len-k
        # remove old start, and add new end, change vowelCount if needed
        # will need to keep a maxVowel count - to not need to count each time w/ O(n*5) i.e. O(n) to count vowel totals each time

        # count vowels in initial window:
        window = s[0:k]
        vowelCount = 0
        for x in window:
            if x in {'a', 'e', 'i', 'o','u'}:
                vowelCount += 1
        maxCount = vowelCount
        for y in range(len(s)-k):
            if s[y] in {'a', 'e', 'i', 'o','u'}:
                vowelCount -= 1
            if s[k+y] in {'a', 'e', 'i', 'o','u'}:
                vowelCount += 1
            if maxCount < vowelCount:
                maxCount = vowelCount 
        return maxCount
