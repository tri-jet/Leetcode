class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for x in range(len(digits)-1, -1, -1):
            currentSum = digits[x] + carry
            digits[x] = currentSum % 10
            carry = currentSum // 10
        if carry:
            digits = [1] + digits
        return digits
