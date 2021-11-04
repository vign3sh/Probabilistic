from grid import *
from probab.astar import *
from probab.examine import *
from probab.utility import *
from agents.agent import *


def call_agent(agents):
    while True:
        grid, start, goal = make_grid(n)
        explored_grid = make_empty_grid(n, goal)
        start_cell = explored_grid[start[0]][start[1]]
        print(start, goal)
        goal_cell = explored_grid[goal[0]][goal[1]]
        if len(a_star(explored_grid, start_cell, goal_cell)) > 0:
            break
    '''
    grid = [[3, 1, 1, 0, 3],
            [2, 3, 0, 1, 0],
            [0, 0, 2, 3, 3],
            [0, 1, 2, 1, 0],
            [3, 1, 3, 2, 0]]
    start = [4, 0]
    goal = [3, 1]
    '''


    # print(start)
    print_grid(grid, n, goal)
    # print_ex_grid(explored_grid, n)
    start_cell = explored_grid[start[0]][start[1]]

    for i in agents:
        examined_cells = set()
        agent_element = Agent(i)
        path = agent_element.agent(start_cell, explored_grid, grid, n, examined_cells)
        '''
        for cell in path:
            print(cell.get_xy())
        '''
        explored_grid = make_empty_grid(n, goal)
        start_cell = explored_grid[start[0]][start[1]]

        # print_pf(explored_grid, n)
        # print_cell_type(explored_grid, n)

# step 1: examine start to get goal state
# step 2: pass the goal state to a-star and get path
# step 3: agent follows path till block or till goal changes and get new goal


n = GLOBAL_BIG_MAZE_SIZE
agent = [6]
call_agent(agent)
