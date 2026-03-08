class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # generate all combos first? then strike off?
        # hint: convert given strings to base 10
        # hmm ok, so n = 2, -> range 00 -> 11 = 00 to 3
        # can loop thru 0 to 2^n -1, find first num that exists in remaining set?

        n = len(nums[0])
        for x in range(0, len(nums)):
            nums[x] = str(int(nums[x],2))
        nums = set(nums)

        for x in range(0, 2**n):
            if str(x) not in nums:

                prefixCount = n - len(bin(x)[2:])
                return "0"*prefixCount + bin(x)[2:]

        # 0 won't show as 0b00, or whatever length.
        # better to convert all nums to base 10 first
        # then compare 0 to 2^n, then add bin padding
        # ex1: n = 2, nums = 1, 2. O not in thus return bin(0)
        # bin(0)[2:] = 0, then prefix w/ 0* n-currentLen
