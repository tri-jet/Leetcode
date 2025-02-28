class Solution:
    
    def isPrefixAndSuffix(self, str1: str, str2: str) -> bool:
        return (str2[0:len(str1)] == str1 and str2[len(str2)-len(str1):] == str1)

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            str1 = words[i] # store as need repeated access of this across j loop
            for j in range(i, len(words)):
                if self.isPrefixAndSuffix(str1, words[j]) and i != j:
                    count += 1

        return count
