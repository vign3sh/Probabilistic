from constants.constants import *
from probab.main import call_agent
import time

no_of_tests = GLOBAL_TEST_COUNT
agent_list = [6, "8-5", "8-10", "8-15"]
total_time = [[] for i in range(len(agent_list))]
total_movements = [[] for i in range(len(agent_list))]
total_examinations = [[] for i in range(len(agent_list))]
for i in range(no_of_tests):
    times, _, movements, examinations = call_agent(agent_list, GLOBAL_BIG_MAZE_SIZE)
    for j in range(len(times)):
        print('Grid Number:', i+1, '   Time for agent_list', agent_list[j], ':', times[j])
        total_time[j].append(times[j])
        total_movements[j].append(movements[j])
        total_examinations[j].append(examinations[j])
    print()

tot_time = [0 for j in range(len(agent_list))]
tot_move = [0 for j in range(len(agent_list))]
tot_exam = [0 for j in range(len(agent_list))]
tot_actions = [0 for j in range(len(agent_list))]
for i in range(no_of_tests):
    for j in range(len(agent_list)):
        tot_time[j] += total_time[j][i]
        tot_move[j] += total_movements[j][i]
        tot_exam[j] += total_examinations[j][i]

for j in range(len(total_time)):
    print('Average Time for agent:', agent_list[j], tot_time[j]/no_of_tests)
    print('Avg examinations: ', tot_exam[j]/no_of_tests)
    print('Avg movements: ', tot_move[j]/no_of_tests)
    print('Avg actions: ', (tot_move[j] + tot_exam[j])/no_of_tests)

print("-------------------------RAW-------------------------------------")
print(total_time)
print(total_examinations)
print(total_movements)

# [[m1, m2, m3, ...m10],[m1, m2, m3, ...m10],[m1, m2, m3, ...m10]]