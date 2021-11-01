

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