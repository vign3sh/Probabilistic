from constants.constants import *
from probab.main import call_agent
import time

no_of_tests = GLOBAL_TEST_COUNT
agent = [6, 7]
total_time = [0 for i in range(len(agent))]
for i in range(no_of_tests):
    times = call_agent(agent, GLOBAL_BIG_MAZE_SIZE)
    for j in range(len(times)):
        print('Grid Number:', i+1, '   Time for agent', j+6, ':', times[j])
        total_time[j] += times[j]
    print()
for j in range(len(total_time)):
    print('Average Time for agent:', j+6, total_time[j]/no_of_tests)
