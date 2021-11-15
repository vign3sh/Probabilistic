from format import get_grid
from probab.grid import *
from probab.astar import *
from probab.examine import *
from probab.utility import *
from agents.agent import *
import time


def call_agent(agents, n):

    grid = get_grid()
    start = [1, 7]
    goal = [7, 0]
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
    '''

    print(start, goal)
    print_grid(grid, n, goal)
    t = []
    examinations = [0 for i in range(len(agents))]
    movements = [0 for i in range(len(agents))]
    for i in agents:
        s = time.perf_counter()
        examined_cells = set()
        explored_grid = make_empty_grid(n, goal)
        start_cell = explored_grid[start[0]][start[1]]
        agent_element = Agent(i)
        path = agent_element.agent(start_cell, explored_grid, grid, n, examined_cells)
        movements[i - 6] += len(path)
        examinations[i - 6] += agent_element.get_examinations()
        for cell in path:
            print(cell.get_xy(), end=' | ')
        print()
        print('End of Agent ', i)
        e = time.perf_counter()
        t.append(e - s)

    print('End')
    return t, goal_cell, movements, examinations

        # print_ex_grid(explored_grid, n)

# step 1: check for block of start , examine start->check for goal
# step 2: while true
# step 3: if goal found end
# step 4 : if goal == start rexamine start
# step 5 : find path
# step 6 : if path not found set max's probablity of goal to zero
# step 7: travel path in for
# step 8 : block found set end for
# step 9 : goal found end func
# step 10 : check for changed max


agent = [6, 7]
times, _, a, b = call_agent(agent, 10)
for j in range(len(times)):
    print('Time for agent', j+6, ':', times[j])
