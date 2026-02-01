class Solution:
    def isThree(self, n: int) -> bool:
        count = 2 # all nums have 1 and itself at least
        # numbers w/ 3 divisors starts from 4?
        if n < 4:
            return False
        for x in range(2,n):
            if n % x == 0:
                count += 1
            if count > 3:
                return False
        return True
