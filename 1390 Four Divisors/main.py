import math
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        finalSum = 0
        for x in nums:
            divisors = []
            for i in range(1, int(math.sqrt(x) + 1)):
                if x % i == 0:
                    divisors.append(i)
                    if i != x/i:
                        divisors.append(int(x/i))
            if len(divisors) == 4:
                finalSum += sum(divisors)
        return int(finalSum)
