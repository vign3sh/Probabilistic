import heapq as heap
from cell import Cell
from agents.agent import Agent
from probab.utility import *

from constants.constants import *

def repeated_astar(grid, start_state, end_state, agent):

    agent = Agent(agent)
    final_path = []
    while True:
        # print(explored_grid)
        path = a_star(grid, start_state, end_state)

        # unable  to solve the maze
        if len(path) == 0:
            print("No path found")
            final_path = []
            return final_path

        if path[len(path) - 1] == end_state:
            # to be implemented
            final_state = agent.follow_path(grid, path)
            add_to_final_path(final_path, final_state, path)
            if final_state == end_state:
                return final_path
            start_state = final_state       


def a_star(grid, start_state, end_state, explored_grid=None):
    priority_queue = []
    setattr(Cell, "__lt__", lambda self, other: check_dist(self, end_state) <= check_dist(other, end_state))
    heap.heappush(priority_queue, start_state)
    closed_list = set()
    queue = list()

    while len(priority_queue) > 0:
        # print_list(priority_queue)
        current_state = heap.heappop(priority_queue)
        closed_list.add(current_state)
        queue.append(current_state)
        if current_state == end_state:
            # print(current_state.x, " Goal ", current_state.y )
            return queue

        children = get_neighbor(current_state, grid, explored_grid)

        if len(children) == 0:
            continue

        for child in children:
            x, y = child.get_xy()
            if grid[x][y] == Block_Terrain or child in closed_list:
                continue

            old_state = get_element_from_list(priority_queue, child)

            if old_state is None:
                heap.heappush(priority_queue, child)
            elif closer_from_start(old_state, child, start_state):
                update_with_child(priority_queue, child, old_state)
    return []


def get_neighbor(state, grid, explored_grid):
    if explored_grid is not None:
        grid = explored_grid
    neighbors = []
    positions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    x, y = state.get_xy()
    for i in positions:
        if len(grid) > x + i[0] >= 0 and len(grid) > y + i[1] >= 0:
            neighbor = grid[x + i[0]][y + i[1]]
            neighbors.append(neighbor)
    return neighbors


def find_path(start_state, end_state):
    path = []
    temp_state = end_state
    while temp_state != start_state:
        path.insert(0, temp_state)
        temp_state = temp_state.parent_state
    return path


def add_to_final_path(final_path, final_state, path):
    for state in path:
        final_path.add(state)
        if state == final_state:
            break
    return final_path


def get_element_from_list(input_list, element):
    for i in input_list:
        if i == element:
            return i
    return None


def closer_from_start(old_state, new_state, start_state):
    return check_dist(start_state, old_state) > check_dist(start_state, new_state)


# Here we are replacing the element to be popped with the last element and removing the last element and then re-heapify
# we hope this logic saves more time then shifting all the elements by one positions to delete the given element
def update_with_child(input_list, key, new_key):
    i = 0
    while i < len(input_list):
        element = input_list[i]
        if element == key:
            input_list[i] = input_list[-1]
            input_list.pop()
            heap.heapify(input_list)
            heap.heappush(input_list, new_key)
            break
        i += 1

