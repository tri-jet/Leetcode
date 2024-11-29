class Solution:
    def reverseWords(self, s: str) -> str:
        # add words to list - removes spaces,
        # then just reverse the list and make it a string w/ spaces
        words = s.split()
        words.reverse()
        return " ".join(words)