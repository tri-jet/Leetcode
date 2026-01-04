class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        #-(a // -b) - a/b but round up as ceil "can quietly produce incorrect results, as it introduces floating-point error"
        finalSum = 0
        for x in nums:
            divisors = []
            for i in range(2, -(x // -2)):
                if x % i == 0:
                    divisors.append(i)
            divisors.append(1)
            if x != 1:
                divisors.append(x)
            if len(divisors) == 4:
                finalSum += sum(divisors)
        return finalSum
