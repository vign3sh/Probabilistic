from constants.constants import *
from probab.cell import Cell
from probab.utility import *


# Call directly whe cell-terrain is already determined
def examine(cell, exp_grid, grid, agent):
    i, j = cell.get_xy()
    check = check_goal(cell)
    if check:
        return "Goal"
    oldpg = cell.get_pg()
    change = cell.get_pf() * oldpg
    cell.set_pg(oldpg - change)

    return change_prob(exp_grid, cell, change, oldpg, agent)


# Called when new block is visited.
def examine_first(cell, exp_grid, grid, agent, examined_cells):
    examined_cells.add(cell)
    # to kow the terrain/block
    terrain_type(cell, exp_grid, grid, agent)
    i = cell.get_xy()[0]
    j = cell.get_xy()[1]
    oldpg = cell.get_pg()

    if cell.get_terrain() == 0:
        cell.set_pg(0)
        change = oldpg
        change_prob(exp_grid, cell, change, oldpg, agent)
        return "Block"

    else:
        cell.set_pg(oldpg / 0.7)
        change = oldpg - cell.get_pg()
        change_prob(exp_grid, cell, change, oldpg, agent)
        # print(cell.get_pg())
        return examine(exp_grid[i][j], exp_grid, grid, agent)


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
    maxProb = cell.get_pg()
    maxCell = [cell]

    for i in range(len(exp_grid)):
        for j in range(len(exp_grid)):
            if not ((i, j) == cell.get_xy()):
                pij = exp_grid[i][j].Pg
                pij = pij + (pij / (1 - pxy)) * change
                exp_grid[i][j].set_pg(pij)
                if agent == 6:
                    if pij > maxProb and (len(maxCell) == 0 or check_dist(cell, maxCell[-1]) > check_dist(cell, exp_grid[i][j])):
                        maxCell.clear()
                        maxCell.append(exp_grid[i][j])
                        maxProb = pij

                    elif pij == maxProb and check_dist(cell, maxCell[-1]) > check_dist(cell, exp_grid[i][j]):
                        maxCell.clear()
                        maxCell.append(exp_grid[i][j])

                    elif pij == maxProb and check_dist(cell, maxCell[-1]) == check_dist(cell, exp_grid[i][j]):
                        maxCell.append(exp_grid[i][j])

    return maxCell[random.randint(0, len(maxCell)-1)]
