class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        l1 = list(word1)
        l2 = list(word2)
        l1.sort()
        l2.sort()
        # if l1 == l2:
        #     return True
        # use unique num of occurrences if occurences match then works?
        # count frequencies of different chars - but doesn't actually matter what they are?
        # e.g. case 3 - cabbba vs abbccc = 1 x c, 2 x a, 3 x b vs 1 x a, 2 x b, 3 x c
        # so do hashmap and check the keys of each match up 
        l1Hash = {}
        l2Hash = {}
        for x in range(0, len(l1)):
            l1Hash.get(l1[x],1)
            l2Hash.get(l2[x],1)
        return l2Hash.keys() == l1Hash.keys()
