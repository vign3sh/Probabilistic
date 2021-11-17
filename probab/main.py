from format import get_grid
from probab.grid import *
from probab.astar import *
from probab.examine import *
from probab.utility import *
from probab.examine_optimal import *
from agents.agent_factory import *
import time


def call_agent(agent_list, n):
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
    # print_full_path(path)
    print()

    print(start, goal)
    print_grid(grid, n, goal)
    t = []
    examinations = [0 for i in range(len(agent_list))]
    movements = [0 for i in range(len(agent_list))]
    for i in range(len(agent_list)):
        s = time.perf_counter()
        examined_cells = set()
        explored_grid = make_empty_grid(n, goal)
        start_cell = explored_grid[start[0]][start[1]]
        agent_element = get_agent(agent_list[i])
        path = agent_element.agent(start_cell, explored_grid, grid, n, examined_cells)
        movements[i] += len(path)
        examinations[i] += agent_element.get_examinations()
        for cell in path:
            print(cell.get_xy(), end=' | ')
        print()
        print('End of Agent ', agent_list[i])
        e = time.perf_counter()
        t.append(e - s)

    print('Vignesh chutiya')
    print(movements)
    print(examinations)
    return t, goal_cell, movements, examinations

'''
agent_list = [6, "8-1", "8-2", 7]
times, _, a, b = call_agent(agent_list, 50)
for j in range(len(times)):
    print('Time for agent', agent_list[j], ':', times[j])
'''