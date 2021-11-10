from format import get_grid
from probab.grid import *
from probab.astar import *
from probab.examine import *
from probab.utility import *
from agents.agent import *
import time


def call_agent(agents, n):
    '''
    grid = get_grid()
    start = [3, 22]
    goal = [5, 5]
    test_grid = make_test_grid(n, goal, grid)
    start_cell = test_grid[start[0]][start[1]]
    goal_cell = test_grid[goal[0]][goal[1]]
    path = a_star(test_grid, start_cell, goal_cell)
    if len(path) == 0:
        print('Not solvable')
        return
    else:
        print_full_path(path)
        print()
    '''
    while True:
        grid, start, goal = make_grid(n)
        test_grid = make_test_grid(n, goal, grid)
        start_cell = test_grid[start[0]][start[1]]
        goal_cell = test_grid[goal[0]][goal[1]]
        path = a_star(test_grid, start_cell, goal_cell)
        if len(path) > 0:
            break
    print('New Grid')
    print_full_path(path)
    print()

    print(start, goal)
    print_grid(grid, n, goal)
    t = []
    for i in agents:
        s = time.perf_counter()
        examined_cells = set()
        explored_grid = make_empty_grid(n, goal)
        start_cell = explored_grid[start[0]][start[1]]
        agent_element = Agent(i)
        path = agent_element.agent(start_cell, explored_grid, grid, n, examined_cells)
        for cell in path:
            print(cell.get_xy(), end=' | ')
        print()
        print('End of Agent ', i)
        e = time.perf_counter()
        t.append(e - s)

    print('End')
    return t, goal_cell

        # print_ex_grid(explored_grid, n)
# step 1: examine start to get goal state
# step 2: pass the goal state to a-star and get path
# step 3: agent follows path till block or till goal changes and get new goal

'''
agent = [6, 7]

times, _ = call_agent(agent, GLOBAL_BIG_MAZE_SIZE)
for j in range(len(times)):
    print('Time for agent', j+6, ':', times[j])
'''