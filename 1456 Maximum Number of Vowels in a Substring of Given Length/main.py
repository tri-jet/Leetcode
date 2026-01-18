class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # at least O(n) - need to check every pos to see max count of vowels in window
        # look at every k letters and count num of vowels - can only range from 0 to k. So if found k then return no point finding more
        # so now count number of vowels in 0 to k first. Then for k to len(s) +1, check if the x-k was a vowel, and if the new last val is
        
        # count number of vowels in initial 0 to k.
        currentCount = 0
        for letter in s[0:k]:
            if letter in {'a','e','i','o','u'}:
                currentCount += 1
        if currentCount == k:
            return k
        maxCount = currentCount
        for x in range(k, len(s)):
            print(f"{s[x-k:x]}, old first = {s[k-x-1]}, new last = {s[x]}")
            # get old first val, and now last val i.e. left and right of window and compare
            if s[x-k-1] in {'a','e','i','o','u'} and s[x] not in {'a','e','i','o','u'}:
                currentCount -= 1
            elif s[x-k-1] not in {'a','e','i','o','u'} and s[x] in {'a','e','i','o','u'}:
                currentCount += 1
            if currentCount == k:
                return k
            maxCount = currentCount if currentCount > maxCount else maxCount
            #print(f"so count now: {count}")

        return maxCount
