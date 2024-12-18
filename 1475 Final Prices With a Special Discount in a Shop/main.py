class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # can i just replace the values in prices instead of making new one?
        # is it better to work my way backwards?
        # e.g. last one -> no discount
        # 2nd last -= last (if last lower)
        # 
        # try brute force first
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                if prices[j] < prices[i]:
                    prices[i] -= prices[j]
                    break

        return prices
