class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        lowest = [] # use monotonic stack for lowest prices
        for i in range(len(prices)-1, -1, -1):
            print(i)
            if not lowest:
                lowest.append(prices[i])
                continue
            else:
                if lowest[-1] <= prices[i]:
                    lowest.append(prices[i])
                    prices[i] -= lowest[-2] 
                else:   # if current price < top of lowest
                    while(lowest and lowest[-1] > prices[i]):   # find val lower than current or till empty
                        lowest.pop()
                    # now should be empty or lowest top < current
                    lowest.append(prices[i])
                    if len(lowest) >= 2:    # if found one lower than current, use as discount
                        prices[i] -= lowest[-2]
                    continue
        return prices   
