class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        # well needs to be O(n^2) as need to find optimal solution + look at all
        maxDist = 0
        for i in range(0, len(nums1)):
            for j in range(0, len(nums2)):
                if i > j:
                    continue
                if nums1[i] > nums2[j]:
                    continue
                maxDist = j-i if j-i > maxDist else maxDist
        return maxDist
