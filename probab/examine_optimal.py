from constants.constants import *
from probab.cell import Cell
from probab.utility import *


# Call directly whe cell-terrain is already determined
def examine(cell, exp_grid):
    check = check_goal(cell)
    if check:
        return "goal", cell
    oldpg = cell.get_pg()
    cell.set_pg(oldpg * (1 - cell.get_pf()))
    # return "continue", change_prob(exp_grid, cell, change, oldpg, agent)
    return "continue", update_prob(exp_grid, cell, oldpg)


# Called when new block is visited.
def examine_first(cell, exp_grid, grid, examined_cells):
    examined_cells.add(cell)
    # to kow the terrain/block
    terrain_type(cell, exp_grid, grid)

    i, j = cell.get_xy()
    oldpg = cell.get_pg()

    if cell.get_terrain() == 0:
        cell.set_pg(0)
        cell.set_terrain(0)
        cell.set_pf(0)
        change = oldpg
        # change_prob(exp_grid, cell, change, oldpg, agent)

        return "block", update_prob(exp_grid, cell, oldpg)

    else:
        cell.set_pg(oldpg / 0.7)
        change = oldpg - cell.get_pg()
        # change_prob(exp_grid, cell, change, oldpg, agent)
        update_prob(exp_grid, cell, oldpg)
        # print(cell.get_pg())
        return examine(exp_grid[i][j], exp_grid)


def terrain_type(cell, exp_grid, grid):

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


# Translate change of probability to all the neighbors
def update_prob(exp_grid, cell, oldpg):

    max_prob = cell.get_pg()

    maxCell = [cell]
    ratio = (1 - cell.get_pg()) / (1 - oldpg)
    for i in range(len(exp_grid)):
        for j in range(len(exp_grid)):
            if not ((i, j) == cell.get_xy()):
                pij = exp_grid[i][j].get_pg()
                pij = pij * ratio
                exp_grid[i][j].set_pg(pij)

                if pij > max_prob:
                    maxCell.clear()
                    maxCell.append(exp_grid[i][j])
                    max_prob = pij

                elif pij == max_prob and check_dist(cell, maxCell[-1]) > check_dist(cell, exp_grid[i][j]):
                    maxCell.clear()
                    maxCell.append(exp_grid[i][j])

                elif pij == max_prob and check_dist(cell, maxCell[-1]) == check_dist(cell, exp_grid[i][j]):
                    maxCell.append(exp_grid[i][j])

    return maxCell[random.randint(0, len(maxCell) - 1)]



