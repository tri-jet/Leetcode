class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # must be relating to modulus of each step?

        students_sum = sum(chalk)
        if k >= students_sum:
            return k % students_sum
        else:
            for x in range(0, len(chalk)):
                if k-chalk[x] < 0:
                    return x
                k -= chalk[x]