import sys

from constants.constants import *
from probab.cell import Cell
from probab.utility import *


# Call directly whe cell-terrain is already determined
def examine(cell, exp_grid, agent):
    i, j = cell.get_xy()
    check = check_goal(cell)
    if check:
        return "goal", cell
    oldpg = cell.get_pg()
    cell.set_pg(oldpg * (1 - cell.get_pf()))
    # return "continue", change_prob(exp_grid, cell, change, oldpg, agent)
    return "continue", update_prob(exp_grid, cell, oldpg, agent)


# Called when new block is visited.
def examine_first(cell, exp_grid, grid, agent, examined_cells):
    examined_cells.add(cell)
    # to kow the terrain/block
    terrain_type(cell, exp_grid, grid, agent)

    i, j = cell.get_xy()
    oldpg = cell.get_pg()

    if cell.get_terrain() == 0:
        cell.set_pg(0)
        cell.set_terrain(0)
        cell.set_pf(0)
        change = oldpg
        # change_prob(exp_grid, cell, change, oldpg, agent)

        return "block", update_prob(exp_grid, cell, oldpg, agent)

    else:
        cell.set_pg(oldpg / 0.7)
        change = oldpg - cell.get_pg()
        # change_prob(exp_grid, cell, change, oldpg, agent)
        update_prob(exp_grid, cell, oldpg, agent)
        # print(cell.get_pg())
        return examine(exp_grid[i][j], exp_grid, agent)


def terrain_type(cell, exp_grid, grid, agent):

    x, y = cell.get_xy()
    if grid[x][y] == Block_Terrain:
        exp_grid[x][y].set_terrain(Block_Terrain)
        exp_grid[x][y].set_pf(0)

    elif grid[x][y] == Flat_Terrain:
        exp_grid[x][y].set_terrain(Flat_Terrain)
        exp_grid[x][y].set_pf(0.8)

    elif grid[x][y] == Hill_Terrain:
        exp_grid[x][y].set_terrain(Hill_Terrain)
        exp_grid[x][y].set_pf(0.5)

    else:
        exp_grid[x][y].set_terrain(Forest_Terrain)
        exp_grid[x][y].set_pf(0.2)


def change_prob(exp_grid, cell, change, pxy, agent) -> Cell:
    """

    :rtype: Cell
    """
    maxProb = 0
    if agent == 6:
        maxProb = cell.get_pg()
    if agent == 7:
        maxProb = cell.get_pfg()

    maxCell = [cell]

    for i in range(len(exp_grid)):
        for j in range(len(exp_grid)):
            if not ((i, j) == cell.get_xy()):
                pij = exp_grid[i][j].Pg
                pij = pij + (pij / (1 - pxy)) * change
                exp_grid[i][j].set_pg(pij)

                if agent == 6:
                    if pij > maxProb:
                        maxCell.clear()
                        maxCell.append(exp_grid[i][j])
                        maxProb = pij

                    elif pij == maxProb and check_dist(cell, maxCell[-1]) > check_dist(cell, exp_grid[i][j]):
                        maxCell.clear()
                        maxCell.append(exp_grid[i][j])

                    elif pij == maxProb and check_dist(cell, maxCell[-1]) == check_dist(cell, exp_grid[i][j]):
                        maxCell.append(exp_grid[i][j])

                if agent == 7:
                    pfg = exp_grid[i][j].get_pfg()
                    if pfg > maxProb:
                        maxCell.clear()
                        maxCell.append(exp_grid[i][j])
                        maxProb = pfg

                    elif pfg == maxProb and check_dist(cell, maxCell[-1]) > check_dist(cell, exp_grid[i][j]):
                        maxCell.clear()
                        maxCell.append(exp_grid[i][j])

                    elif pfg == maxProb and check_dist(cell, maxCell[-1]) == check_dist(cell, exp_grid[i][j]):
                        maxCell.append(exp_grid[i][j])

    return maxCell[random.randint(0, len(maxCell)-1)]


# Translate change of probability to all the neighbors
def update_prob(exp_grid, cell, oldpg, agent):

    max_prob6 = cell.get_pg()
    max_prob7 = cell.get_pfg()

    maxCell = [cell]

    # ratio of (1-new p of current cell) / (1-old p of current cell)
    ratio = (1 - cell.get_pg())/(1 - oldpg)
    print(ratio)
    if ratio == 1.0:
        sys.exit(0)
    for i in range(len(exp_grid)):
        for j in range(len(exp_grid)):
            if not ((i, j) == cell.get_xy()):
                pij = exp_grid[i][j].get_pg()
                pij = pij * ratio
                exp_grid[i][j].set_pg(pij)

                if agent == 6:
                    if pij > max_prob6:
                        maxCell.clear()
                        maxCell.append(exp_grid[i][j])
                        max_prob6 = pij

                    elif pij == max_prob6 and check_dist(cell, maxCell[-1]) > check_dist(cell, exp_grid[i][j]):
                        maxCell.clear()
                        maxCell.append(exp_grid[i][j])

                    elif pij == max_prob6 and check_dist(cell, maxCell[-1]) == check_dist(cell, exp_grid[i][j]):
                        maxCell.append(exp_grid[i][j])

                if agent == 7:
                    pfg = exp_grid[i][j].get_pfg()
                    if pfg > max_prob7:
                        maxCell.clear()
                        maxCell.append(exp_grid[i][j])
                        max_prob7 = pfg

                    elif pfg == max_prob7 and check_dist(cell, maxCell[-1]) > check_dist(cell, exp_grid[i][j]):
                        maxCell.clear()
                        maxCell.append(exp_grid[i][j])

                    elif pfg == max_prob7 and check_dist(cell, maxCell[-1]) == check_dist(cell, exp_grid[i][j]):
                        maxCell.append(exp_grid[i][j])
    for c in maxCell:
        print(c.get_xy())
    return maxCell[random.randint(0, len(maxCell) - 1)]



