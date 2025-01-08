class Solution:
    
    def isPrefixAndSuffix(self, str1: str, str2: str) -> bool:
        # can convert to 1 line
        if str2[0:len(str1)] == str1 and str2[len(str2)-len(str1):] == str1:
            return True
        else: return False

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        if(self.isPrefixAndSuffix(words[0],words[1])):
            return 1
        else: return 0
    
