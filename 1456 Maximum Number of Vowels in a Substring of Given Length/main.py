class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # at least O(n) - need to check every pos to see max count of vowels in window
        # look at every k letters and count num of vowels - can only range from 0 to k. So if found k then return no point finding more
        count = 0
        for x in range(k, len(s)):
            
            print(s[x-k:x])
            current = 0
            for letter in s[x-k:x]:
                
                if letter in ['a','e','i','o','u']:
                    current += 1
                
                print(f"letter: {letter}, current: {current}")
            print(f"ending search of {s[x-k:x]}, current was {current}, count previously {count}")
            count = current if current > count else count
            print(f"so count now: {count}")

        return count
