from probab.utility import *
import random
from probab.cell import Cell


def get_max(cell, exp_grid, agent, closed_list=None):
    maxProb6 = cell.get_pg()
    maxProb7 = cell.get_pfg()
    maxCell = [cell]
    l = len(exp_grid)
    for i in range(0, l):
        for j in range(0, l):
            if agent == 6:
                pij = exp_grid[i][j].get_pg()
                if pij > maxProb6:
                    maxCell.clear()
                    maxCell.append(exp_grid[i][j])
                    maxProb6 = pij

                elif pij == maxProb6 and check_dist(cell, maxCell[-1]) > check_dist(cell, exp_grid[i][j]):
                    maxCell.clear()
                    maxCell.append(exp_grid[i][j])

                elif pij == maxProb6 and check_dist(cell, maxCell[-1]) == check_dist(cell, exp_grid[i][j]):
                    maxCell.append(exp_grid[i][j])

            if agent == 7:
                pfg = exp_grid[i][j].get_pfg()
                if pfg > maxProb7:
                    maxCell.clear()
                    maxCell.append(exp_grid[i][j])
                    maxProb7 = pfg

                elif pfg == maxProb7 and check_dist(cell, maxCell[-1]) > check_dist(cell, exp_grid[i][j]):
                    maxCell.clear()
                    maxCell.append(exp_grid[i][j])

                elif pfg == maxProb7 and check_dist(cell, maxCell[-1]) == check_dist(cell, exp_grid[i][j]):
                    maxCell.append(exp_grid[i][j])

    return maxCell[random.randint(0, len(maxCell) - 1)]
