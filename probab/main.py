from grid import Grid
from probab.examine import *
from probab.utility import *
from agents.agent import *


def call_agent(agents):
    # grid, start, goal = Grid.make_grid(n)
    grid = [[3, 1, 1, 0, 3],
            [2, 3, 0, 1, 0],
            [0, 0, 2, 3, 3],
            [0, 1, 2, 1, 0],
            [3, 1, 3, 2, 0]]
    start = [4, 0]
    goal = [3, 1]
    explored_grid = Grid.make_empty_grid(n, goal)
    examined_cells = set()
    # print(start)
    print_grid(grid, n, goal)
    # print_ex_grid(explored_grid, n)
    start_cell = explored_grid[start[0]][start[1]]
    for i in agents:
        agent_element = Agent(i)
        path = agent_element.agent(start_cell, explored_grid, grid, n, examined_cells)

        for cell in path:
            print(cell.getxy())

# step 1: examine start to get goal state
# step 2: pass the goal state to a-star and get path
# step 3: agent follows path till block or till goal changes and get new goal

n = GLOBAL_SMALL_MAZE_SIZE
agent = [6]
call_agent(agent)
