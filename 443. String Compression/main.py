class Solution:
    def compress(self, chars: List[str]) -> int:
        current = chars[0]
        currentCount = 1
        i = 1
        while i <  len(chars):
            print(len(chars))
            if chars[i] == current:
                chars.pop(i)
                currentCount += 1
            else:
                chars.insert(i,str(currentCount))
                current = chars[i]
                currentCount = 1
                i+=2
        if currentCount > 1:
            chars.append(str(currentCount))
        return len(chars)
            