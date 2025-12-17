class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # what happens if size is 0? - ah isn't possible
        # spent time figuring out way to check xor of both vars 
        # ah looking at the examples 1 pass from the left might not work acc
        asteroidStack = []
        for x in asteroids:
            print(asteroidStack)
            if len(asteroidStack) == 0:
                asteroidStack.append(x)
                continue
            if asteroidStack[-1]*x < 0: # if both have diff signs, then result always negative
                if abs(asteroidStack[-1]) > abs(x):
                    continue
                elif abs(asteroidStack[-1]) == abs(x):
                    continue
                else: 
                    asteroidStack.pop()
                    asteroidStack.append(x)
            else: asteroidStack.append(x)
        return asteroidStack
