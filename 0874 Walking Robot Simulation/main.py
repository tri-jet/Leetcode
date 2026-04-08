class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        pos = [0,0]
        directions = ["N", "E", "S","W"]    
        facing = 0  # corresponds to N in directions
        for command in commands:
            if command >= 1 and command <= 9:
                match directions[facing]:
                    case "N":
                        pos[1] += command
                    case "E":
                        pos[0] += command
                    case "S":
                        pos[1] -= command
                    case "W":
                        pos[0] -= command
            elif command == -2:
                facing -= 1
            elif command == -1:
                facing += 1
        return pos[0]^2 + pos[1]^2
