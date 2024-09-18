class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        all_words = s1.split(" ") + s2.split(" ")

        words_set = set()
        for word in all_words:
            if word in words_set:
                words_set.remove(word)
            else: words_set.add(word)
        return list(words_set)
