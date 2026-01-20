class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for x in range(0, len(strs)):
            word = list(strs[x])
            word.sort()
            word = str(word)
            #anagrams[word] = anagrams.get(anagrams[word],strs[x]).append(strs[x])
            # if sorted word exists in anagrams, then add to list, else create new key
            if word in anagrams:
                anagrams[word].append(strs[x])
            else: anagrams[word] = [strs[x]]
        return list(anagrams.values())
