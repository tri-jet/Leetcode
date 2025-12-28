class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # sort them 
        # select from end in descending order, add to sum, increment pickCount i.e. first time 0 ->1
        # repeat till pickCount = k, and also when picking child, subtract pickCount from their happiness
        happiness.sort()
        picked = 0
        happySum = 0
        while picked < k:
            happySum += happiness[-1-picked]-picked if happiness[-1-picked]-picked > 0 else 0
            picked += 1
        return happySum
