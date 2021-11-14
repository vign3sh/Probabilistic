from probab.examine import *
from probab.astar import *
from probab.getmax import get_max
from probab.utility import *


class Agent:

    def __init__(self, number):
        self.type = number

    def agent(self, start_cell, explored_grid, grid, n, examined_cells):
        final_path = [start_cell]

        get_terrain_type(start_cell, explored_grid, grid, self.type, examined_cells)
        is_goal = examine(start_cell, explored_grid, self.type)
        while True:

            goal_cell = get_max(start_cell, explored_grid, self.type)
            if is_goal:
                # final_path.append(goal_cell)
                return final_path

            print(start_cell.get_xy(), '->', goal_cell.get_xy())

            # print_ex_grid(explored_grid, n)
            # max_cell = get_max(start_cell, explored_grid, n, i)
            # print(max_cell.get_xy(), start)

            # If we have start cell as goal cell examine again
            if goal_cell == start_cell:
                is_goal = examine(start_cell, explored_grid, self.type)
                # print("Goal in start cell", goal_cell.get_pg())
                continue

            reset_astar_param(explored_grid)
            path = a_star(explored_grid, start_cell, goal_cell)

            # No path from start to probable goal that means probable goal is not the goal
            if len(path) == 0:
                print("No path found")
                update_block_prob(goal_cell, explored_grid, self.type)
                # final_path = []
                # return final_path
                continue

            path.insert(0, start_cell)
            # print("Path")
            # print_full_path(path)
            for i in range(1, len(path)):
                cell = path[i]
                # print(cell.get_xy())

                if cell not in examined_cells:
                    terrain_type = get_terrain_type(cell, explored_grid, grid, self.type, examined_cells)
                else:
                    terrain_type = cell.get_terrain()
                # print(terrain_type, cell.get_xy())
                # Block Found Start Cell changed to it's parent
                if terrain_type == Block_Terrain:
                    print('Blocked  :', cell.get_xy())
                    update_block_prob(goal_cell, explored_grid, self.type)
                    # path[i-1] is examined and we are reexamining at start state again
                    # goal_cell = start_cell
                    break

                # Goal Found Exit Agent
                if cell == goal_cell:
                    is_goal = examine(cell, explored_grid, self.agent)
                    if is_goal:
                        final_path.append(cell)
                        return final_path

                start_cell = cell
                final_path.append(cell)

                '''
                if self.type == 7:
                    if cell.get_pfg() > goal_cell.get_pfg():
                        break
                '''

