class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        finalSum = 0
        for x in nums:
            divisors = []
            for i in range(2, int(x/2) + 1):
                if x % i == 0:
                    divisors.append(i)
            divisors.append(1)
            if x != 1:
                divisors.append(x)
            if len(divisors) == 4:
                finalSum += sum(divisors)
        return finalSum
