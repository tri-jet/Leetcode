class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            for x in range(len(grid[0])):
                if row[x] < 0:
                    count += len(grid[0])-x
                    break
        return count
