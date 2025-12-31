class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            start = 0
            end = len(grid)-1
            first_neg = len(grid[0])

            while start <= end:
                mid = (start + end) //2
                if row[mid] < 0:
                    first_neg = mid
                    end = mid - 1
                else: start = mid + 1
            count += len(grid[0]) - first_neg
        return count
