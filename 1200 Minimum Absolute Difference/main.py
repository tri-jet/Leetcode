class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # sort?
        # find minimum abs difference? 
        arr.sort()
        pairs = []
        minDiff = float("inf")
        for x in range(1, len(arr)):
            if arr[x] - arr[x-1] < minDiff:
                minDiff = arr[x] - arr[x-1]
        # has to be O(n) anyways so fine if I loop thru again
        for y in range(1, len(arr)):
            if arr[y] - arr[y-1] == minDiff:
                pairs.append([arr[y-1],arr[y]])
        return pairs
