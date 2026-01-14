class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # at least O(n) - need to check every pos to see max count of vowels in window
        # look at every k letters and count num of vowels - can only range from 0 to k. So if found k then return no point finding more
        count = 0
        for x in range(k, len(s)+1):
            #print(f"{s[x-k:x]} - which is x-k: {x-k} to x: {x}")
            current = 0
            for letter in s[x-k:x]:
                if letter in ['a','e','i','o','u']:
                    current += 1
                if current == k:
                    return k
                #print(f"letter: {letter}, current: {current}")
            #print(f"ending search of {s[x-k:x]}, current was {current}, count previously {count}")
            count = current if current > count else count
            #print(f"so count now: {count}")

        return count

# so for some reason unable to do last 7 chars of weallloveyou k = 7 i.e. loveyou - i.e. 4
# len of "weallloveyou" is 12
# x in range k to len -> so that's 7 to 12. but that's actually 
