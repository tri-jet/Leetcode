import re
class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        # coupon validity - needs number at start - \w works actually from re instead of using all the types
        # put in separate lists, then .sort each at end, then append in business line order.
        # use full match as search means it looks for just anything matching - so search \w+ would look for any matches for word characters
        # And w means look for 1 word character, \w+ means 1 or more
        validElec = []
        validGroc = []
        validPharm = []
        validRest = []

        for x in range(len(code)):
            if code[x] == "":
                continue
            if re.fullmatch(r"\w+", code[x]):
                if isActive[x]:
                    match businessLine[x]:
                        case "electronics":
                            validElec.append(code[x])
                        case "grocery":
                            validGroc.append(code[x])
                        case "pharmacy":
                            validPharm.append(code[x])
                        case "restaurant":
                            validRest.append(code[x])
        return validElec + validGroc + validPharm + validRest
