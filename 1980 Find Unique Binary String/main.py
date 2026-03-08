class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # generate all combos first? then strike off?
        # hint: convert given strings to base 10
        # hmm ok, so n = 2, -> range 00 -> 11 = 00 to 3
        # can loop thru 0 to 2^n -1, find first num that exists in remaining set?

        n = len(nums[0])
        print(n)
        print(2**n)
        limit = 2**n # n=3 range = 0 to 7, range(a, b) goes from a to b-1 anyways 
        nums = set(nums)    # check if in = O(1)
        for x in range(0, limit):
            print(f"x:{x}, bin={bin(x)[2:]}")
            if x == 0:
                if "0"*n not in nums:
                    return "0"*n
            elif bin(x)[2:] not in nums:
                return bin(x)[2:]

        # 0 won't show as 0b00, or whatever length.
