class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while(len(stones) > 1):
            print(stones)
            if(stones[0] == stones[1]):
                stones.pop(0)
                stones.pop(0)
            else:
                stones[0] -= stones[1]
                stones.pop(1)
                stones.sort()
        if(len(stones) == 1):
            return stones[0]
        if(len(stones) == 0):
            return 0
