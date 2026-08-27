
import math
import random



class vacuum_gird:
    def __init__(rows = 5, cols = 5):
        self.rows = rows
        self.cols = cols

        # Create a grid, and randomly initilize each cell, 0 = clean, 1 = dirty
        self.grid = [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]
        # Designate the starting cell for the vacuum

        self.row = random.randint (0, rows-1)
        self.col = random.randint (0, cols-1)

    pass



class vacuum_action(grid):
 
    def move(self):
        pass


    def suck(self):
        if grid[row, col] == 0:
            move()
        elif grid[row, col] == 1:
            grid[row, col] = 0
            move()




class vacuum_goal:
    pass


def main():

    vacumm