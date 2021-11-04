from main.utility import *
from cell import Cell
import random

def get_max(cell, exp_grid, n, agent):
    max_cell = [cell]
    for i in range(n):
        for j in range(n):
            if agent == 6 and exp_grid[i][j].get_terrain() != 0:
                if exp_grid[i][j].get_pg() > max_cell[-1].get_pg():
                    max_cell.clear()
                    max_cell.append(exp_grid[i][j])
                elif exp_grid[i][j].get_pg() == max_cell[-1].get_pg() and not(i == cell.get_xy()[0] and j == cell.get_xy()[1]):
                    dist = check_distance(cell, exp_grid[i][j], max_cell[-1])
                    if dist > 0:
                        max_cell.clear()
                        max_cell.append(exp_grid[i][j])
                    elif dist == 0:
                        max_cell.append(exp_grid[i][j])
                    else:
                        continue

    for i in max_cell:
        print(i.get_xy())

    if max_cell[0] == cell:
        return max_cell[0]

    return max_cell[random.randint(0, len(max_cell)-1)]

