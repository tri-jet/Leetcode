class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        l1 = list(word1)
        l2 = list(word2)
        l1.sort()
        l2.sort()
        print(f"L1: {l1}, \n L2: {l2}")
        if l1 == l2:
            return True
        # use unique num of occurrences if occurences match then works?
        # count frequencies of different chars - but doesn't actually matter what they are?
        # e.g. case 3 - cabbba vs abbccc = 1 x c, 2 x a, 3 x b vs 1 x a, 2 x b, 3 x c
        # so do hashmap and check the keys of each match up 
        # ah should be the values anyways, but still why no keys??
        l1Hash = {}
        l2Hash = {}
        for x in range(0, len(l1)):
            l1Hash[l1[x]] = l1Hash.get(l1[x],0) + 1
            l2Hash[l2[x]] = l2Hash.get(l2[x],0) + 1
            print(f"l1 current: {l1[x]}")
            print(f"l2 current: {l2[x]}")
        print(f"{l1Hash.keys()} and values: {l1Hash.values()}")
        print(f"{l2Hash.keys()} and values: {l2Hash.values()}")   # printed empty?? for both
        l1 = list(l2Hash.values())
        l1.sort()
        l2 = list(l1Hash.values())
        l2.sort()
        print(f"now l1: {l1} now l2: {l2}")
        return l1 == l2

        # failed for cabbba and aabbss - output was true
        # cabbba = 1c, 2a, 3b vs aabbss = 2a 2b 2s 
