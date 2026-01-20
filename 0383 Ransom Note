class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag =  {}
        for x in magazine:
            mag[x] = mag.get(x,0) + 1
        for x in ransomNote:
            if x not in mag:
                return False
            else:
                if mag.get(x) == 0:
                    return False
                else: mag[x] = mag.get(x) - 1
        return True
