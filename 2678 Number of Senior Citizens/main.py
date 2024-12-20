class Solution:
    def countSeniors(self, details: List[str]) -> int:
        seniors = 0
        for passenger in details:
            if int(passenger[11:13]) > 60:
                seniors += 1
        return seniors
