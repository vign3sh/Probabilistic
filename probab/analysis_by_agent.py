from constants.constants import *
from probab.main import call_agent
import time

no_of_tests = GLOBAL_TEST_COUNT
agent = [6, 7]
flat_time = [0 for i in range(len(agent))]
hill_time = [0 for j in range(len(agent))]
forest_time = [0 for k in range(len(agent))]
flat_count = 0
hill_count = 0
forest_count = 0
for i in range(no_of_tests):
    times, goal_cell = call_agent(agent, GLOBAL_MED_MAZE_SIZE)
    for j in range(len(times)):
        print('Grid Number:', i+1, '   Time for agent', j+6, ':', times[j])
        if goal_cell.terrain == Flat_Terrain:
            flat_time[j] += times[j]
            flat_count += 1
        if goal_cell.terrain == Hill_Terrain:
            hill_time[j] += times[j]
            hill_count += 1
        if goal_cell.terrain == Forest_Terrain:
            forest_time[j] += times[j]
            forest_count += 1
    print()
for j in range(len(agent)):
    print('Average Time for agent in flat terrain:', j+6, flat_time[j]/flat_count)
    print('Average Time for agent in hill terrain:', j+6, hill_time[j]/hill_count)
    print('Average Time for agent in forest terrain:', j+6, forest_time[j]/forest_count)
