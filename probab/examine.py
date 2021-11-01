from constants.constants import *
import random
from probab.utility import *


def examine(cell, exp_grid, grid):
    i, j = cell.get_xy()
    check = check_goal(cell)
    if check:
        return "Goal"
    oldpg = cell.get_pg()
    change = cell.get_pf() * oldpg
    cell.set_pg(oldpg - change)
    change_prob(exp_grid, i, j, change, oldpg)
    return 'Go Ahead'


# Used directly from terrain type when new block is visited
def examine_first(cell, exp_grid, grid):
    i = cell.get_xy()[0]
    j = cell.get_xy()[1]
    oldpg = cell.get_pg()

    if cell.get_terrain() == 0:
        cell.set_pg(0)
        change = oldpg
        change_prob(exp_grid, i, j, change, oldpg)
        return "Block"

    else:
        cell.set_pg(oldpg / 0.7)
        change = oldpg - cell.get_pg()
        change_prob(exp_grid, i, j, change, oldpg)
        print(cell.get_pg())
        return examine(exp_grid[i][j], exp_grid, grid)


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
    return examine_first(exp_grid[x][y], exp_grid, grid)


def change_prob(exp_grid, x, y, change, pxy):
    # maxPro = 0
    # maxCell = null
    for i in range(len(exp_grid)):
        for j in range(len(exp_grid)):
            if not (i == x and y == j):
                pij = exp_grid[i][j].Pg
                pij = pij + (pij / (1 - pxy)) * change
                exp_grid[i][j].set_pg(pij)
                # if pij > maxPron and dist(xy, targ) > dist(ij, targ):
                # maxcell = ij
                # maxprob = pij
