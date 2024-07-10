class Solution:
    def minOperations(self, logs: List[str]) -> int:
        dist = 0

        for log in logs:
            if log == "../":
                if dist > 0:
                    dist -= 1   # if outside of main, then moving to parent is closer to main folder 
            elif log == "./":
                dist += 0 # doesn't change folders so no change in distance
            else: dist += 1 # don't need regex as only 3 operation formats possible.
        return dist