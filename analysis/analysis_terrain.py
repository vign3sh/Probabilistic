from constants.constants import *
from probab.main import call_agent
import time

no_of_tests = GLOBAL_TEST_COUNT
agent_list = [6, "8-5", "8-10", "8-15"]

flat_time = [[] for i in range(len(agent_list))]
hill_time = [[] for i in range(len(agent_list))]
forest_time = [[] for i in range(len(agent_list))]
flat_examination = [[] for i in range(len(agent_list))]
hill_examination = [[] for i in range(len(agent_list))]
forest_examination = [[] for i in range(len(agent_list))]
flat_movements = [[] for i in range(len(agent_list))]
hill_movements = [[] for i in range(len(agent_list))]
forest_movements = [[] for i in range(len(agent_list))]

flat_count = 0
hill_count = 0
forest_count = 0
for i in range(no_of_tests):
    times, goal_cell, movements, examinations = call_agent(agent_list, GLOBAL_BIG_MAZE_SIZE)
    for j in range(len(agent_list)):
        print('Grid Number:', i+1, '   Time for agent', agent_list[j], ':', times[j])
        if goal_cell.terrain == Flat_Terrain:
            flat_time[j].append(times[j])
            flat_movements[j].append(movements[j])
            flat_examination[j].append(examinations[j])
            flat_count += 1
            print("vignesh chutiya")
            print(flat_movements)
            print(flat_examination)
        if goal_cell.terrain == Hill_Terrain:
            hill_time[j].append(times[j])
            hill_movements[j].append(movements[j])
            hill_examination[j].append(examinations[j])
            hill_count += 1
        if goal_cell.terrain == Forest_Terrain:
            forest_time[j].append(times[j])
            forest_movements[j].append(movements[j])
            forest_examination[j].append(examinations[j])
            forest_count += 1
    print()

flat_count = int(flat_count/4)
hill_count = int(hill_count/4)
forest_count = int(forest_count/4)

tot_flat_time = [0 for j in range(len(agent_list))]
tot_flat_move = [0 for j in range(len(agent_list))]
tot_flat_exam = [0 for j in range(len(agent_list))]

tot_hill_time = [0 for j in range(len(agent_list))]
tot_hill_move = [0 for j in range(len(agent_list))]
tot_hill_exam = [0 for j in range(len(agent_list))]

tot_forest_time = [0 for j in range(len(agent_list))]
tot_forest_move = [0 for j in range(len(agent_list))]
tot_forest_exam = [0 for j in range(len(agent_list))]

print(flat_time)
print(flat_count)
for i in range(flat_count):
    for j in range(len(agent_list)):
        tot_flat_time[j] += flat_time[j][i]
        tot_flat_move[j] += flat_movements[j][i]
        tot_flat_exam[j] += flat_examination[j][i]

for i in range(hill_count):
    for j in range(len(agent_list)):
        tot_hill_time[j] += hill_time[j][i]
        tot_hill_move[j] += hill_movements[j][i]
        tot_hill_exam[j] += hill_examination[j][i]

for i in range(forest_count):
    for j in range(len(agent_list)):
        tot_forest_time[j] += forest_time[j][i]
        tot_forest_move[j] += forest_movements[j][i]
        tot_forest_exam[j] += forest_examination[j][i]

for j in range(len(agent_list)):
    print('Average Time for agent in flat terrain:', agent_list[j], tot_flat_time[j]/flat_count)
    print('Average Time for agent in hill terrain:', agent_list[j], tot_hill_time[j]/hill_count)
    print('Average Time for agent in forest terrain:', agent_list[j], tot_forest_time[j]/forest_count)
    print('Average Movements for agent in flat terrain:', agent_list[j], tot_flat_move[j]/flat_count)
    print('Average Movements for agent in hill terrain:', agent_list[j], tot_hill_move[j]/hill_count)
    print('Average Movements for agent in forest terrain:', agent_list[j], tot_forest_move[j]/forest_count)
    print('Average Examinations for agent in flat terrain:', agent_list[j], tot_flat_exam[j]/flat_count)
    print('Average Examinations for agent in hill terrain:', agent_list[j], tot_hill_exam[j]/hill_count)
    print('Average Examinations for agent in forest terrain:', agent_list[j], tot_forest_exam[j]/forest_count)
    print('Average Actions for agent in flat terrain:', agent_list[j], (tot_flat_move[j] + tot_flat_exam[j])/flat_count)
    print('Average Actions for agent in hill terrain:', agent_list[j], (tot_hill_move[j] + tot_hill_exam[j])/hill_count)
    print('Average Actions for agent in forest terrain:', agent_list[j], (tot_forest_move[j] + tot_forest_exam[j])/forest_count)

# call_agent [[ag1, ag2, ag3], [ag1,ag2, ag3]]
# scatter plot of raw data
# bar graph of raw data
