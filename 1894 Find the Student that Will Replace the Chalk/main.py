class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        students_sum = sum(chalk)
        if k >= students_sum:
            k %= students_sum
        for x in range(0, len(chalk)):
            if k-chalk[x] < 0:
                return x
            k -= chalk[x]