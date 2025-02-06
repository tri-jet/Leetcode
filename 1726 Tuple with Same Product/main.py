class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # check multiples of each pair? then maths from there?
        # 2 - 6, 8, 12
        # 3 - 6, 12, 18
        # 4 - 8, 12, 24
        # 6 - 12, 18, 24 
        # all have common multiple of 12 
        # if ab = cd, then we have ba = cd,
        # ab = dc, ba = dc 

        products = {}
        
        for x in nums:
            for y in nums:
                if x == y:
                    continue
            if x*y in products:
                products[x*y] = products[x*y].append(tuple(x,y))
            else:
                products[x*y] = [(x,y)]
        
        print(products)

        return 8
