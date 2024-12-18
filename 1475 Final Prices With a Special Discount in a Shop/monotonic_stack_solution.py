class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        lowest = [] # use monotonic stack for lowest prices
        for i in range(len(prices)-1, -1):
            # if lowest empty (starting at end)
            if not lowest:
                lowest.append(prices[i])
                continue
            
            # if current is lower than closest low price
            if prices[i] < lowest[-1]:
                # remove any vals higher than current and add current instead
                while(lowest[-1] > prices[i]):
                    lowest.pop()
                prices.append(prices[i])
                continue
            
            # if current >= closest low price, subtract discount, lowest stays same
            if prices[i] >= lowest[-1]:
                prices[i] -= lowest[-1]
                continue
        
        return prices   
