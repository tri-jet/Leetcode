from fractions import Fraction
class Solution:
    def fractionAddition(self, expression: str) -> str:
        result = 0.0
        for x in range(0, len(expression)):
            if expression[x] == "+":
                result += float(expression[x+1]) / float (expression[x+3])
            if expression[x] == "-":
                result -= float(expression[x+1]) / float (expression[x+3])
            x += 3
            continue
        print(result)
        return str(Fraction(result))