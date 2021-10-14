import random as rd

class SimpleExplorer:

    def __init__(self, arrow) -> None:
        self.position = [0,0]
        self.arrows = arrow
        self.gold = 0
        self.wumpus_kills = 0
        self.death_by_pit = 0
        self.death_by_wumpus = 0
        self.visited_cells = []
        self.cost = 0
        self.moves = 0
        self.direction = "north"
        self.screamHeard = False
    
    def getCurrentCell(self, board):
        return board.getCell(self.position)
    
    def getCurrentState(self, cell):
        return cell.getState()

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
        # print(self.direction)
        self.cost -= 1
    
    def directedTurn(self, direction):
        self.direction = direction
        self.cost -= 1
    
    
    def moveForward(self, board):
        old_position = self.position

        if self.direction == "north" and self.position[0] - 1 >= 0:
            self.position = [self.position[0] - 1, self.position[1]]

        if self.direction == "south" and self.position[0] + 1 <= board.getSize()-1:
            self.position = [self.position[0] + 1, self.position[1]]

        if self.direction == "east" and self.position[1] + 1 <= board.getSize()-1:
            self.position = [self.position[0], self.position[1] + 1]

        if self.direction == "west" and self.position[1] - 1 >= 0:
            self.position = [self.position[0], self.position[1] - 1]

        cell = board.getCell(self.position)

        if cell.getState()['Obstacle'] == True:
            self.position = old_position

        self.cost -= 1
        self.moves += 1
        
    def shootArrow(self, board):
        if self.arrows > 0:
            self.arrows -= 1
            self.cost -= 50

            arrow_pos = self.position
            

            if self.direction == "north":
                while arrow_pos[0] > 0:
                    arrow_pos = [arrow_pos[0] - 1, arrow_pos[1]]
                    self.arrow_fire(board, arrow_pos)

            if self.direction == "south":
                while arrow_pos[0] < board.getSize()-1:
                    arrow_pos = [arrow_pos[0] + 1, arrow_pos[1]]
                    self.arrow_fire(board, arrow_pos)

            if self.direction == "east":
                while arrow_pos[1] < board.getSize()-1:
                    arrow_pos = [arrow_pos[0], arrow_pos[1] + 1]
                    self.arrow_fire(board, arrow_pos)

            if self.direction == "west":
                while arrow_pos[1] > 0:
                    arrow_pos = [arrow_pos[0] -1, arrow_pos[1] - 1]
                    self.arrow_fire(board, arrow_pos)

        return False
    
    def arrow_fire(self, board, arrow_pos):
        arrow_cell_state = self.getCurrentState(board.getCell(arrow_pos))
        if arrow_cell_state['Wumpus'] == True:
            self.screamHeard = True
            self.wumpus_kills += 1
            return True
        if arrow_cell_state['Obstacle'] == True:
            return False

    def getPosition(self):
        return self.position
    
    def determineDeath(self, cell):
        state = self.getCurrentState(cell)     

        if state['Wumpus'] == True:
            # print("Killed by a stinking wumpus")
            self.death_by_wumpus += 1
            return True
        elif state['Pit'] == True:
            # print("Fell into a pit")
            self.death_by_pit += 1
            return True
        
        return False

    def determineWin(self, cell):
        state = self.getCurrentState(cell)

        if state['Gold'] == True:
            # self.simple_board.getCell(cell.getIndex()).setStateGold()
            self.gold += 1
            return True
        
        return False

    def simpleSearchForGold(self, board):
        while(self.moves <= board.getSize() * board.getSize()):
            
            cell = board.getCell(self.position)

            if cell not in self.visited_cells:
                self.visited_cells.append(cell)
            # print(self.position)
            if self.determineDeath(cell) == True:
                self.cost -= 1000
                # print("Lost Board")
                break
            
            if self.determineWin(cell) == True:
                self.cost += 1000
                # self.simple_board.displaySimpleBoard(board.getSize())
                # print("Won Board")
                break

            if rd.random() > 0.98:
                self.shootArrow(board)

            if (self.screamHeard == True):
                # print("SCREAM HEARD")
                self.screamHeard = False

            self.turn()
            self.moveForward(board)
            cell = board.getCell(self.position)



        # board.displayBoard(board.getSize())
        # print()
        # self.simple_board.displaySimpleBoard(board.getSize())
        return {"Cost": self.cost, 
                "Total Moves": self.moves, 
                "Wumpuses Killed": self.wumpus_kills,
                "Death by Wumpus": self.death_by_wumpus,
                "Death by Pit": self.death_by_pit, 
                "Gold Captured": self.gold, 
                "Total Visited Cells": len(self.visited_cells)}