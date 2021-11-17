from probab.examine_optimal import *
from probab.astar import *
from probab.utility import *


class AgentNew:

    def __init__(self, threshold):
        self.type = 8
        self.examinations = 0
        self.final_path = []
        self.threshold = threshold

    def agent(self, start_cell, explored_grid, grid, n, examined_cells):
        self.final_path = [start_cell]
        while True:
            if start_cell not in examined_cells:
                next_step, goal_cell = examine_first(start_cell, explored_grid, grid, examined_cells)
            else:
                next_step, goal_cell = examine(start_cell, explored_grid)
            self.examinations += 1

            # Goal Found

            if next_step == 'goal':
                # self.final_path.append(goal_cell)
                return self.final_path

            print(start_cell.get_xy(), '->', goal_cell.get_xy())

            # print_cell_type(explored_grid, n)
            # max_cell = get_max(start_cell, explored_grid, n, i)
            # print(max_cell.get_xy(), start)

            # If we have start cell as goal cell examine again
            if goal_cell == start_cell:
                # print("Goal in start cell", goal_cell.get_pg())
                continue

            reset_astar_param(explored_grid)
            path = a_star(explored_grid, start_cell, goal_cell)

            # No path from start to probable goal that means probable goal is not the goal
            if len(path) == 0:
                print("No path found")
                oldpg = goal_cell.get_pg()
                goal_cell.set_pg(0)
                update_prob(explored_grid, goal_cell, oldpg)
                # self.final_path = []
                # return self.final_path
                continue

            path.insert(0, start_cell)
            # print("Path")
            # print_full_path(path)
            if len(path) > self.threshold:
                start_cell = self.examine_all_cells(start_cell, path, explored_grid, grid, examined_cells)
                if start_cell is None:
                    return self.final_path
            else:
                start_cell = self.examine_last_cell(start_cell, path, explored_grid, grid, examined_cells)
                if start_cell is None:
                    return self.final_path
            '''if max_cell.get_xy() != goal_cell.get_xy():
                 break'''

    def examine_all_cells(self, start_cell, path, explored_grid, grid, examined_cells):
        for i in range(1, len(path)):
            cell = path[i]
            if cell not in examined_cells:
                next_step, max_cell = examine_first(cell, explored_grid, grid, examined_cells)
            else:
                next_step, max_cell = examine(cell, explored_grid)
            self.examinations += 1

            # print(next_step, cell.get_xy())
            # Block Found Start Cell changed to it's parent
            if next_step == 'block':
                # print('Blocked  :', cell.get_xy())
                # path[i-1] is examined and we are reexamining at start state again
                start_cell = path[i - 1]
                # goal_cell = start_cell
                break

            # Goal Found Exit Agent
            elif next_step == 'goal':
                self.final_path.append(cell)
                return None
            start_cell = cell
            self.final_path.append(cell)
        return start_cell

    def examine_last_cell(self, start_cell, path, explored_grid, grid, examined_cells):
        for i in range(1, len(path)):
            cell = path[i]
            terrain_type(cell, explored_grid, grid)
            # print(next_step, cell.get_xy())
            # Block Found Start Cell changed to it's parent
            if cell.get_terrain() == Block_Terrain:
                update_prob(explored_grid, cell, cell.get_pg())
                # print('Blocked  :', cell.get_xy())
                # path[i-1] is examined and we are reexamining at start state again
                start_cell = path[i - 1]
                # goal_cell = start_cell
                break

            # Goal Found Exit Agent
            elif i == len(path) - 1:
                if cell not in examined_cells:
                    next_step, max_cell = examine_first(cell, explored_grid, grid, examined_cells)
                else:
                    next_step, max_cell = examine(cell, explored_grid)
                self.examinations += 1
                self.final_path.append(cell)
                if next_step == 'goal':
                    return None
            start_cell = cell
            self.final_path.append(cell)
        return start_cell

    def get_examinations(self):
        return self.examinations

    @staticmethod
    def get_agent_type():
        return 8
