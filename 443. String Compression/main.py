class Solution:
    def compress(self, chars: List[str]) -> int:
        s = []
        current = s[0]
        s.append(current)
        currentCount = 1
        for i in range(1, len(s)):
            if s[i] == current:
                currentCount += 1
            if s[i] != current:
                if currentCount > 1:
                    s.append(str(currentCount))
                    currentCount = 1
                current = s[i]
                s.append(s[i])
                