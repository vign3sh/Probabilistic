import heapq as heap
from probab.cell import Cell
from probab.utility import *
from constants.constants import *


def a_star(grid, start_state, end_state):
    priority_queue = []
    setattr(Cell, "__lt__", lambda self, other: check_dist(self, end_state) <= check_dist(other, end_state))
    heap.heappush(priority_queue, start_state)
    closed_list = set()

    while len(priority_queue) > 0:
        current_state = heap.heappop(priority_queue)
        # print(current_state.get_xy())
        closed_list.add(current_state)

        if current_state == end_state:
            # print(current_state.X, " Goal ", current_state.Y)
            return find_path(start_state, current_state)

        children = get_neighbor(current_state, grid, closed_list)

        if len(children) == 0:
            continue

        for child in children:
            if child in closed_list:
                continue

            old_state = get_element_from_list(priority_queue, child)

            if old_state is None:
                heap.heappush(priority_queue, child)
            elif closer_from_start(old_state, child):
                update_with_child(priority_queue, child, old_state)
    return []


def get_neighbor(state, grid, closed_list):
    neighbors = []
    positions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    x, y = state.get_xy()
    for i in positions:
        new_x = x + i[0]
        new_y = y + i[1]
        if len(grid) > new_x >= 0 and len(grid) > new_y >= 0 and grid[new_x][new_y].get_terrain() != Block_Terrain:
            neighbor = grid[new_x][new_y]
            if neighbor not in closed_list:
                neighbor.set_parent(state)
            neighbor.set_gx(state.get_gx() + 1)
            neighbors.append(neighbor)
    return neighbors


def find_path(start_state, end_state):
    path = []
    temp_state = end_state
    while temp_state != start_state:
        # print(temp_state.X, " In path", temp_state.Y)
        path.insert(0, temp_state)
        temp_state = temp_state.parent
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


def closer_from_start(old_state, new_state):
    return old_state.get_gx() > new_state.get_gx()


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

