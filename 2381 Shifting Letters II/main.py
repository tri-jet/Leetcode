class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # use char int values 
        # use ord on each alphabet, do +/-, then use chr() on letter
        # more efficient
        # have list for length of string, with 0s,
        # go thru shifts, put +/- 1 on indices, to figure out total shift?
        for shift in shifts:
            print(shift)
            for i in range(shift[0], shift[1]+1):
                print(f"letter: {s[i]} position: {ord(s[i])-96}")

        return s
