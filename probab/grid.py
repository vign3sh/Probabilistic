import random
from cell import Cell


class Grid:
    start = []
    goal = []

    @staticmethod
    def make_grid(n):
        grid = [[0 for i in range(n)] for j in range(n)]
        # print(grid)
        for i in range(0, n):
            for j in range(0, n):
                p = random.uniform(0, 1)
                if p <= 0.3:
                    grid[i][j] = 0
                elif 0.3 < p <= 0.5333:
                    grid[i][j] = 1
                elif 0.5333 < p < 0.7666:
                    grid[i][j] = 2
                else:
                    grid[i][j] = 3

        while True:
            i = random.randint(0, n-1)
            j = random.randint(0, n-1)

            if grid[i][j] != 0:
                goal = [i, j]
                break

        while True:
            i = random.randint(0, n - 1)
            j = random.randint(0, n - 1)

            if grid[i][j] != 0 and not(i == goal[0] and j == goal[1]):
                start = [i, j]
                break
        return grid, start, goal

    @staticmethod
    def make_empty_grid(n, goal):
        g = [[Cell for i in range(n)] for j in range(n)]
        # print(grid)
        for i in range(0, n):
            for j in range(0, n):
                g[i][j] = Cell(i, j, -1, 0.35, 1 / (n * n))
                if i == goal[0] and j == goal[1]:
                    g[i][j].set_target()

        return g

'''

import random
import Cell


class Grid:
    def __init__(self, n):
        self.N = n
        self.grid = []
        self.flatP = 0.2
        self.hillP = 0.5
        self.forestP = 0.8
        self.generateGrid()

    def generateGrid(self):
        for i in range(self.N):
            for j in range(self.N):
                rNum = random.random()
                # [0.0,0.2)
                if 0 <= rNum < self.flatP:
                    cell = Cell(1, 0.9, self.N)
                    self.grid.append(cell)
                # [0.2,0.5)
                elif self.flatP <= rNum < self.flatP + self.hillP:
                    cell = Cell(2, 0.7)
                    self.grid.append(cell)
                # [0.5,0.8)
                elif self.flatP + self.hillP <= rNum < self.flatP + self.hillP + self.forestP:
                    cell = Cell(3, 0.3)
                    self.grid.append(cell)
                # [0.8,1.0)
                else:
                    cell = Cell(4, 0.1)
                    self.grid.append(cell)

        success = True
        while success:
            targetI = random.randint(0, 49)
            targetJ = random.randint(0, 49)
            if self.getCell(targetI, targetJ).terrain == 3:
                self.getCell(targetI, targetJ).isTarget = True
                # print('Target is in: ', '[', targetI, ',', targetJ, ']')
                success = False

        #print('Target is in: ', '[', targetI, ',', targetJ, ']')
        #self.getCell(targetI, targetJ).isTarget = True

    def getCell(self, x, y):
        return self.grid[x * self.N + y]
'''
