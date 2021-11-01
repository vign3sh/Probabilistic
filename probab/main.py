
from grid import Grid
from probab.examine import *
from probab.utility import *


def call_agent(agent):
    grid, start, goal = Grid.make_grid(n)
    explored_grid = Grid.make_empty_grid(n, goal)
    examined_cells=set()

    #print(start)
    print_grid(grid, n, goal)
    print_ex_grid(explored_grid, n)
    start_cell = explored_grid[start[0]][start[1]]
    examined_cells.add(start_cell)
    result = examine(start_cell, explored_grid, grid)
    if result == 'Go Ahead':
        print_ex_grid(explored_grid, n)
        print_cell_type(explored_grid, n)

    '''for i in agent:
        max_cell = get_max(start, agent, explored_grid)
    '''

n = GLOBAL_SMALL_MAZE_SIZE
agent = [6]
call_agent(agent)
