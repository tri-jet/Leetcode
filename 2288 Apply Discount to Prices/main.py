import re
class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        # all words split by spaces
        # doesn't say if initial prices can include decimals - assuming not then
        if not discount:
            return sentence
        words = sentence.split()
        for x in range(0, len(words)):
            # ^  = start, \$ = dollar sign, \d+ = one or more digits, $  = end of the word
            priceFound = re.search(r"^\$\d+$",words[x])
            if priceFound:
                price = float(priceFound.string[1:])
                newPrice = price - price*discount/100
                words[x] = f"${newPrice:.2f}"
        return " ".join(words)
