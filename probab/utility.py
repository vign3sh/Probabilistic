import random

def print_ex_grid(g, n):
    for i in range(n):
        for j in range(n):
            if g[i][j].get_target():
                print('(', g[i][j].get_pg(), ',*) ', end='')
            else:
                print(g[i][j].get_pg(), ' ', end='')
        print()


def print_grid(g, n, goal):
    for i in range(n):
        print('[', end='')
        for j in range(n):
            if i == goal[0] and j == goal[1]:
                print('(', g[i][j], ',*), ', end='')
            else:
                print(g[i][j], ', ', end='')
        print(']')


def print_cell_type(g, n):
    for i in range(n):
        for j in range(n):
            if g[i][j].get_target():
                print('(', g[i][j].get_terrain(), ',*) ', end='')
            else:
                print(g[i][j].get_terrain(), ' ', end='')
        print()


def print_pf(g, n):
    for i in range(n):
        for j in range(n):
            if g[i][j].get_target():
                print('(', g[i][j].get_pf(), ',Target) ', end='')
            else:
                print(g[i][j].get_pf(), ' ', end='')
        print()


def check_distance(cell, current_cell, max_cell):
    # Return more than zero if current cell is closer than max cell
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
        print('Goal ', val, 'vs', cell.get_pf())
        if val < cell.get_pf():
            return True
    return False


def print_path(path):
    for state in path:
        print(state.get_xy())


def find_path(start_state, end_state):
    path = []
    temp_state = end_state
    print(temp_state.get_xy())
    while temp_state != start_state:
        path.insert(0, temp_state)
        temp_state = temp_state.get_parent()
    return path


def print_full_path(path):
    for state in path:
        print(state.X, ",", state.Y, end="  ")


def reset_astar_param(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            grid[i][j].set_parent(None)
            grid[i][j].set_gx(0)
