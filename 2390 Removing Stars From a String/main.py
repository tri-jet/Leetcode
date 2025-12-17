class Solution:
    def removeStars(self, s: str) -> str:
        # stack problem so
        # go thru s start to end, add chars to stack
        # if current == *, then pop top character, continue
        stack = []
        for char in s:
            if char == "*":
                stack.pop()
            else: stack.append(char)
        return "".join(stack) 
