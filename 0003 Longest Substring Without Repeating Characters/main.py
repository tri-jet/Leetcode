class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 1
        maxLen = 0
        if len(s) == 1 or len(s) == 0:
            return len(s)
        found = {}
        while(start < len(s)-1) and end < len(s)):
            currentLen = 1
            found = {s[start]}
            noDupes = True
            while(noDupes and end < len(s)):
                if s[end] not in found:
                    found.add(s[end])
                    currentLen += 1
                    end += 1
                else:
                    # dupe found
                    start += 1
                    end = start + 1
                    noDupes = False
		maxLen = currentLen if currentLen > maxLen else maxLen
        return maxLen