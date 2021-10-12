import random as rd

class SimpleExplorer:

    def __init__(self, position, arrow) -> None:
        self.position = position
        self.arrows = arrow
        self.gold = 0
        self.wumpus_kills = 0
        self.death_by_pit = 0
        self.death_by_wumpus = 0
        self.total_cells_explored = 0
        self.cost = 0
        self.direction = "north"
    

    def turn(self):
        num = rd.random()
        if(num < 0.25):
            self.direction = "north"
        elif(num < 0.5):
            self.direction = "south"
        elif(num < 0.75):
            self.direction = "east"
        elif(num > 0.75):
            self.direction = "west"
        print(self.direction)
        self.cost -= 1
    
    def directedTurn(self, direction):
        self.direction = direction
        self.cost -= 1
    
    def moveForward(self):
        if self.direction == "north":
            self.position = [self.position[0] - 1, self.position[1]]
        if self.direction == "south":
            self.position = [self.position[0] + 1, self.position[1]]
        if self.direction == "east":
            self.position = [self.position[0], self.position[1] + 1]
        if self.direction == "west":
            self.position = [self.position[0], self.position[1] - 1]
        
        self.cost -= 1
        print(self.position)
        
        
    
    def getPosition(self):
        return self.position

