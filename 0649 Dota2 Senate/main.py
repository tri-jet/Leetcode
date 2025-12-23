class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # if equal count then first to come across wins
        # if inequal count, then higher wins
        if senate.count("R") == senate.count("D"):
            if senate[0] == "R":
                return "Radiant"
            else: return "Dire"
        else:
            if senate.count("R") > senate.count("D"):
                return "Radiant"
            else: return "Dire"
