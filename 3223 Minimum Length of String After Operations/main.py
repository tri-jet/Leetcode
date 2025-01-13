class Solution:
    def minimumLength(self, s: str) -> int:
        # so basically remove 2 of a letter from a middle position of the same letter
        # i.e. ababa - choose i = 2 - then first and last a can be removed -> bab

        letterCount = {}
        for letter in s:
            if not letterCount.get(letter):
                letterCount.update({letter:1})
            else: letterCount.update({letter:letterCount.get(letter)+1})

        print(letterCount)
        stringLen = len(s)
        for key in letterCount:
            print(letterCount[key])
            keyCount = letterCount[key]
            while(keyCount > 2):
                stringLen -= 2
                keyCount -= 2

        return stringLen
