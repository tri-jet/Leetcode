class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # if diff indices -> if all vals equal = good
        # dist = diff between first and 2nd index, diff between 2nd and 3rd index, and diff 1st and last index
        # make a hashmap, for each val, if 2 others found, then calc dist. If any other good tuples found, then compare dists
        goodTuples = dict()
        minDist = -1
        for x in range(0, len(nums)):
            if nums[x] not in goodTuples:
                goodTuples[nums[x]] = [x]
            else:
                if len(goodTuples.get(nums[x])) < 3:
                    goodTuples[nums[x]].append(x)
                    print(f"Adding at: {x}, and nums[x] is now: {goodTuples[nums[x]]}")
                if len(goodTuples.get(nums[x])) == 3:
                    dist = goodTuples.get(nums[x])[1]-goodTuples.get(nums[x])[0] + x -goodTuples.get(nums[x])[1] + x - goodTuples.get(nums[x])[0]
                    print(f"dist w/ val being {nums[x]} is: {dist}")
                    if minDist == -1:
                        minDist = dist
                    elif dist < minDist:
                        minDist = dist
        print(goodTuples)
        return minDist
