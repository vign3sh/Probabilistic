from constants.constants import *
from probab.main import call_agent
import time


agent = [6]
total_time = 0
for i in range(GLOBAL_TEST_COUNT):
    start = time.perf_counter()
    call_agent(agent, GLOBAL_BIG_MAZE_SIZE)
    end = time.perf_counter()
    total_time += end - start
    print()
    print('Time:', end - start)
print(total_time/GLOBAL_TEST_COUNT)
