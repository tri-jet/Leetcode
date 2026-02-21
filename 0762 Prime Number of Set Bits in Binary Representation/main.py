class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # ok hint helped
        # don't need to check all primes
        # numbers 0 to 10^6 - i.e. a million.
        # a million in binary is 0b11110100001001000000 -> = 20 digits (excluding prefix 0b)
        primes = {2,3,5,7,11,13,17,19}
        primeSetBitCount = 0
        for x in range(left, right + 1):
            bits = bin(x)[2:]
            if self.countBits(bits) in primes:
                primeSetBitCount += 1

        return primeSetBitCount

    def countBits(self, binStr: str) -> int:
        # e.g. "110"
        count = 0
        for x in binStr:
            if x == "1":
                count += 1
        return count
