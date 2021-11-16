from constants.constants import *
from probab.main import call_agent
import time

no_of_tests = 20
agent = 6
threshold = [THRESHOLD_1, THRESHOLD_2, THRESHOLD_3]
total_time = [[] for i in range(len(threshold))]
total_movements = [[] for i in range(len(threshold))]
total_examinations = [[] for i in range(len(threshold))]
for i in range(no_of_tests):
    times, _, movements, examinations = call_agent(GLOBAL_BIG_MAZE_SIZE, threshold)
    for j in range(len(times)):
        print('Grid Number:', i+1, '   Time for threshold', j, ':', times[j])
        total_time[j].append(times[j])
        total_movements[j].append(movements[j])
        total_examinations[j].append(examinations[j])
    print()
for j in range(len(total_time)):
    print('Average Time for agent:', j+6, sum(total_time[j])/no_of_tests)
    print('Avg examinations: ', sum(total_examinations[j])/no_of_tests)
    print('Avg movements: ', sum(total_movements[j])/no_of_tests)
    print('Avg actions: ', (sum(total_examinations[j]) + sum(total_movements[j]))/no_of_tests)

print("-------------------------RAW-------------------------------------")
print(total_time)
print(total_examinations)
print(total_movements)

