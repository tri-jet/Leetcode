class Robot:
    def __init__(self, width: int, height: int):
        self.facing = "East"
        self.pos = [0,0] 
        self.width = width
        self.height = height

    def step(self, num: int) -> None:
        if self.getDir() == "East":
            if self.getPos()[0] + num >= self.width-1:
                newSteps = self.width-1-self.getPos()[0]
                self.pos[0] = self.width-1
                self.facing = "North"
                self.step(newSteps)
            else:
                self.pos[0] += num
                print(f"pos after moving east {num} steps {self.pos}")
        elif self.getDir() == "North":
            if self.getPos()[1] + num >= self.height-1:
                newSteps = self.height-1-self.getPos()[1]
                self.pos[1] = self.height-1
                self.facing = "West"
                self.step(newSteps)
            else:
                self.pos[1] += num
        elif self.getDir() == "West":
            if self.getPos()[0] - num <= 0:
                newSteps = num-self.getPos()[0]
                self.pos[0] = 0
                self.facing = "South"
                self.step(newSteps)
            else:
                self.pos[0] -= num
        elif self.getDir() == "South":
            if self.getPos()[1] - num <= 0:
                newSteps = num-self.getPos()[1]
                self.pos[1] = 0
                self.facing = "East"
                self.step(newSteps)
            else:
                self.pos[1] -= num
        print(f"pos: {str(self.pos)}")

    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        return self.facing


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
