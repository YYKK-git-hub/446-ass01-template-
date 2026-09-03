# // Youkang Shen
# // CSCI 446 Fall 2026
# // Programming Assignment #1
# // I declare that I am the author of this work, take full responsibility for it, and have disclosed any material external assistance.



# This code is structured by myself, but I used Gemini for assistanting in coding, such as initializing the grid, vacuum moving logic, and the randomly move logic.

import math
import random

class vacuum_grid:
    def __init__(self, rows=5, cols=5):
        self.rows = rows
        self.cols = cols
        # Create a grid, and randomly initialize each cell, 0 = clean, 1 = dirty
        self.grid = [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]
        # Designate the starting cell for the vacuum
        self.row = random.randint(0, rows-1)
        self.col = random.randint(0, cols-1)

    def show_grid(self):
        # Optional helper to visualize the grid
        for r in self.grid:
            print(r)
        print(f"Vacuum is currently at ({self.row}, {self.col})\n")


class vacuum_action:
    def __init__(self, env):
        self.env = env

    def move(self):
        directions = []
        # Check boundaries so the vacuum doesn't fall off the grid
        if self.env.row > 0: directions.append("up")
        if self.env.row < self.env.rows - 1: directions.append("down")
        if self.env.col > 0: directions.append("left")
        if self.env.col < self.env.cols - 1: directions.append("right")

        choice = random.choice(directions)
        if choice == "up": self.env.row -= 1
        elif choice == "down": self.env.row += 1
        elif choice == "left": self.env.col -= 1
        elif choice == "right": self.env.col += 1
        
        print(f"Moved {choice} to ({self.env.row}, {self.env.col})")

    def suck(self):
        r = self.env.row
        c = self.env.col
        
        if self.env.grid[r][c] == 1:
            print(f"Cell ({r}, {c}) is dirty. Cleaning it (suck).")
            self.env.grid[r][c] = 0
        else:
            self.move()


class vacuum_goal:
    def __init__(self, env):
        self.env = env
        
    def check_clean(self):
        # Scan the grid. If any cell is 1, return False.
        for row in self.env.grid:
            if 1 in row:
                return False
        return True


def main():
    env = vacuum_grid(5, 5)
    action = vacuum_action(env)
    goal = vacuum_goal(env)

    print("--- Starting Status ---")
    env.show_grid()

    # The reactive loop
    while not goal.check_clean():
        action.suck()
        
    print("\n--- Final Status ---")
    print("Goal achieved: All cells are clean!")
    env.show_grid()

if __name__ == "__main__":
    main()
