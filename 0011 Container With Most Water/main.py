class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end = 0, len(heights) - 1
        mostWater = 0
        while(start < end):
            currentWater = abs(start-end)*heights[start] if heights[start] < heights[end] else abs(start-end)*heights[end]
            mostWater = currentWater if currentWater > mostWater else mostWater
            if heights[start] < heights[end]:
                start += 1
            else: end -= 1
        return mostWater
