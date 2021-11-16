from format import get_grid
from probab.grid import *
from probab.astar import *
from probab.examine import *
from probab.utility import *
from agents.agent import *
from agents.agent_optimal import *
from probab.examine_optimal import *

import time


def call_agent(n, threshold=None):
    '''
    grid = get_grid()
    start = [30, 6]
    goal = [36, 4]
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
    if threshold is None:
        threshold = [4]
    t = []
    examinations = [0 for i in range(len(threshold))]
    movements = [0 for i in range(len(threshold))]
    for i in range(len(threshold)):
        s = time.perf_counter()
        examined_cells = set()
        explored_grid = make_empty_grid(n, goal)
        start_cell = explored_grid[start[0]][start[1]]
        agent_element = Agent(threshold[i])
        path = agent_element.agent(start_cell, explored_grid, grid, n, examined_cells)
        movements[i] += len(path)
        examinations[i] += agent_element.get_examinations()
        for cell in path:
            print(cell.get_xy(), end=' | ')
        print()
        print('End of Agent ', i)
        e = time.perf_counter()
        t.append(e - s)

    print('End')
    return t, goal_cell, movements, examinations


agent = [6, 7]
times, _, a, b = call_agent(agent, 10)
for j in range(len(times)):
    print('Time for agent', j+6, ':', times[j])
