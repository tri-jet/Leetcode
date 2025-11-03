class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        if len(bank) == 1:
            return 0
        startRowCount = bank[0].count("1")
        endRowCount = 0
        totalLasers = 0
        for row in range(1, len(bank)):
            print(f"firstRow {startRowCount} endRow {endRowCount}")
            if endRowCount == 0:
                endRowCount = bank[row].count("1")
            else:
                totalLasers += startRowCount * endRowCount
                startRowCount = endRowCount
                endRowCount = 0
            print(f"end of step: firstRow {startRowCount} endRow {endRowCount}, total {totalLasers}")
        return totalLasers
