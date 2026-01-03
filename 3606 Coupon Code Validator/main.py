class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        # coupon validity = isidentifier - unless includes start w/ number - will try with this first
        # put in separate lists, then .sort each at end, then append in business line order.
        validElec = []
        validGroc = []
        validPharm = []
        validRest = []

        for x in range(len(code)):
            if code[x].isidentifier():
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
        validElec.append(validGroc)
        validElec.append(validPharm)
        validElec.append(validRest)
        return validElec
