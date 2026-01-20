class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        pt = []
        # start from back or front? feels like back is best but might not make an actual difference
        for x in range(len(s)-1, -1, -1):
            if s[x] == "]":
                stack.append(s[x])
            elif s[x].isalpha():
                if len(stack) == 0:
                    pt.append(s[x])
                else:
                    stack.append(s[x])
            elif s[x] == "[":
                stack.append(s[x])
            elif s[x].isdigit():
                # loop between top of stack till
                # everything between 
                enc_string = ""
                while stack[-1] != "]":
                    if stack[-1] == "[":
                        stack.pop()
                        continue
                    enc_string += stack.pop()
                stack.pop()
                for num in range(0, int(s[x])):
                    pt.append(enc_string)
                
        return "".join(pt[::-1])
