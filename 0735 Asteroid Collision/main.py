class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # go backwards
        # if going backwards, then if top is pos & current is neg, then might be inflection
        # if top is negative & current is pos -> collision
        stack = []
        for x in range(len(asteroids)-1,-1,-1):
            if len(stack) == 0:
                stack.append(asteroids[x])
                continue
            if stack[-1] < 0 and asteroids[x] > 0:
                if abs(stack[-1]) > abs(asteroids[x]):
                    continue
                if abs(stack[-1]) == abs(asteroids[x]):
                    stack.pop()
                    continue
                if abs(stack[-1]) < abs(asteroids[x]):
                    stack.pop()
                    stack.append(asteroids[x])
                    continue
            stack.append(asteroids[x])
        return stack[::-1]