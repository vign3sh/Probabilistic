from constants.constants import *
from probab.main import call_agent
import time


agent = [6]
total_time = 0
for i in range(GLOBAL_TEST_COUNT):

    start = time.time()
    call_agent(agent, GLOBAL_BIG_MAZE_SIZE)
    end = time.time()
    total_time += end - start
    print('Time:', end - start)
print(total_time/GLOBAL_TEST_COUNT)
