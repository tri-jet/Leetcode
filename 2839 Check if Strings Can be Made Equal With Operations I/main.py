class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # can swap chars 2 apart - so 0,2 and 1,3
        # do we just check if indices at 0,2 and 1,3 are the same tuples?
        # ex1: abcd, cdab
        # 0,2 = a,c vs c,a
        # 1,3 = b,d vs d,b
        if set([s1[0], s1[2]]) != set([s2[0],s2[2]]):
            return False
        elif set([s1[1], s1[3]]) != set([s2[1], s2[3]]):
            return False
        return True
