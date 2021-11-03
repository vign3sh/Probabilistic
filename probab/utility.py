import random

def print_ex_grid(g, n):
    for i in range(n):
        for j in range(n):
            if g[i][j].get_target():
                print('(', g[i][j].get_pg(), ',Target) ', end='')
            else:
                print(g[i][j].get_pg(), ' ', end='')
        print()


def print_grid(g, n, goal):
    for i in range(n):
        for j in range(n):
            if i == goal[0] and j == goal[1]:
                print('(', g[i][j], ',Target) ', end='')
            else:
                print(g[i][j], ' ', end='')
        print()


def print_cell_type(g, n):
    for i in range(n):
        for j in range(n):
            if g[i][j].get_target():
                print('(', g[i][j].get_terrain(), ',Target) ', end='')
            else:
                print(g[i][j].get_terrain(), ' ', end='')
        print()


def check_distance(cell, current_cell, max_cell):
    #Return more than zero if current cell is closer than max cell
    dist1 = 0
    dist2 = 0
    for i in range(2):
        dist1 += abs(cell.get_xy()[i]-current_cell.get_xy()[i])
        dist2 += abs(cell.get_xy()[i]-max_cell.get_xy()[i])

    return dist2-dist1


def check_dist(a, b):
    return abs(a.get_xy()[0] - b.get_xy()[0]) + abs(a.get_xy()[1] - b.get_xy()[1])


def check_goal(cell):
    val = random.uniform(0, 1)
    if cell.get_target():
        if val < cell.get_pf():
            return True
    return False


def print_path(path):
    for state in path:
        print(state.get_xy())
