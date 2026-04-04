class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        # can I do this mathematically w/o traversing a graph?
        # trim the spaces = "chiepr"
        # c -> i = 0 -> 2, i -> p = 2 -> 4
        # so add each letter with a modulus - so text += [ (0 + rows-1) % len(enc)] 
        # mod ensures it loops round
        # so p -> h = 4 -> 0 = (4 + 2) mod 6 = 0 
        # ah okay so maybe add a visited set - so move 1 up if done? or if index + rows-1 > len, then set to 1? or basically keep count of rows covered
        visited = set()
        text = ""
        index = 0
        encodedText = encodedText.replace(" ","")
        for _ in range(0, len(encodedText)):
            text += encodedText[index]
            visited.add(index)
            index = (index + rows-1) % len(encodedText)
            if index in visited:
                index+=1
        return text
