import heapq as heap
from probab.cell import Cell
from probab.utility import *
from constants.constants import *


def a_star(grid, start_state, end_state):
    priority_queue = []
    setattr(Cell, "__lt__", lambda self, other: check_dist(self, end_state) <= check_dist(other, end_state))
    heap.heappush(priority_queue, start_state)
    closed_list = set()
    path = list()

    while len(priority_queue) > 0:
        # print_list(priority_queue)
        current_state = heap.heappop(priority_queue)
        closed_list.add(current_state)
        path.append(current_state)
        if current_state == end_state:
            # print(current_state.x, " Goal ", current_state.y )
            return path

        children = get_neighbor(current_state, grid)

        if len(children) == 0:
            continue

        for child in children:
            x, y = child.get_xy()
            if child.get_terrain() == Block_Terrain or child in closed_list:
                continue

            old_state_idx = get_element_from_list(priority_queue, child)

            if old_state_idx is None:
                heap.heappush(priority_queue, child)
            elif closer_from_start(old_state_idx, child, start_state):
                update_with_child(priority_queue, child, old_state_idx)
    return []


def get_neighbor(state, grid):
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

