class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_count = 0
        for word in words:
            is_allowed = True
            for letter in word:
                if letter not in allowed:
                    is_allowed = False
            if is_allowed:
                allowed_count += 1

        return allowed_count