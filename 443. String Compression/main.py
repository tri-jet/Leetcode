class Solution:
    def compress(self, chars: List[str]) -> int:
        current = chars[0]
        currentCount = 1
        for i in range(1, charsLen):
            if chars[i] == current:
                chars.pop(i)
                currentCount += 1
                # if currentCount > 10:
            else:
                current = chars[i]
                chars.insert(i-1, str(currentCount))
                currentCount = 1
        if currentCount > 1:
            chars.append(str(currentCount))
        return len(chars)


 # excludes if count > 10 + needs to add count if at end 