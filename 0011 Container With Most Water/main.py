class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # 6 empty bars = 36 ah okay - only in the gaps not above the bars

        # could calc area for any two bars? so it only depends on height and width
        # so ex1: 7 at h[1] and 6 at h[7] -> 6 * (7-1)
        # get all pairs and calculate all possible water contained - then use highest (brute force)
        mostWater = 0
        for i in range(0, len(heights)):
            for j in range(0, len(heights)):
                if i == j:
                    continue
                currentWater = abs(i-j)*heights[i] if heights[i] < heights[j] else abs(i-j)*heights[j]
                mostWater = currentWater if currentWater > mostWater else mostWater
        return mostWater
