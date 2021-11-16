from constants.constants import *
from probab.utility import *


# Call directly whe cell-terrain is already determined
def examine(cell, exp_grid, agent, goal_count):
    if check_goal(cell):
        return True
    elif cell.get_terrain() == Flat_Terrain and goal_count >= 2:
        return True
    elif cell.get_terrain() == Hill_Terrain  and goal_count >= 5:
        return True
    elif cell.get_terrain() == Forest_Terrain  and goal_count >= 8:
        return True
    oldpg = cell.get_pg()
    denom = ((1-oldpg)+ oldpg*cell.get_pf())
    cell.set_pg(oldpg * cell.get_pf()/ denom)
    # return "continue", change_prob(exp_grid, cell, change, oldpg, agent)
    update_prob(exp_grid, cell, denom)
    return False


def get_terrain_type(cell, exp_grid, grid, agent, examined_cells):
    x, y = cell.get_xy()
    examined_cells.add(cell)
    if grid[x][y] == Block_Terrain:
        exp_grid[x][y].set_terrain(Block_Terrain)
        exp_grid[x][y].set_pf(0)

    elif grid[x][y] == Flat_Terrain:
        exp_grid[x][y].set_terrain(Flat_Terrain)
        exp_grid[x][y].set_pf(0.2)

    elif grid[x][y] == Hill_Terrain:
        exp_grid[x][y].set_terrain(Hill_Terrain)
        exp_grid[x][y].set_pf(0.5)

    else:
        exp_grid[x][y].set_terrain(Forest_Terrain)
        exp_grid[x][y].set_pf(0.8)

    return grid[x][y]


def update_block_prob(cell, exp_grid):
    oldpg = cell.get_pg()
    cell.set_pg(0)

    for i in range(len(exp_grid)):
        for j in range(len(exp_grid)):
            if not ((i, j) == cell.get_xy()):
                pij = exp_grid[i][j].get_pg()
                pij = pij / (1-oldpg)
                exp_grid[i][j].set_pg(pij)


# Translate change of probability to all the neighbors
def update_prob(exp_grid, cell, denom):
    for i in range(len(exp_grid)):
        for j in range(len(exp_grid)):
            if not ((i, j) == cell.get_xy()):
                pij = exp_grid[i][j].get_pg()
                exp_grid[i][j].set_pg(pij/denom)




''' Redundant code
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
'''