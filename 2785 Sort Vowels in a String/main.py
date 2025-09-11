class Solution:
    def sortVowels(self, s: str) -> str:
        # so basically re-sort the vowels - their positions. 
        # e.g. if vowels at 3, 5 and 7, then ensure the one at 3 is lower in ascii value than 5.
        # ASCII values are basically alphabetical
        vowels = []
        vowelsIndex = []
        newStr = []
        for x in range(0, len(s)):
            if s[x] in ['a', 'e', 'i', 'o', 'u'] or s[x] in ['A', 'E', 'I','O','U']:
                vowels.append(s[x])
                vowelsIndex.append(x)
                newStr.append("_")
            else: newStr.append(s[x])

        vowels.sort()
        for i in range(0, len(vowelsIndex)):
            newStr[vowelsIndex[i]] = vowels[i]
        return "".join(newStr)
