from probab.examine import *
from probab.astar import *
from probab.utility import *


class Agent:

    def __init__(self, number):
        self.type = number

    def agent(self, start_cell, explored_grid, grid, n, examined_cells):
        final_path = [start_cell]
        if start_cell not in examined_cells:
            next_step, goal_cell = examine_first(start_cell, explored_grid, grid, self.type, examined_cells)
        else:
            next_step, goal_cell = examine(start_cell, explored_grid, self.type)
        while True:
            '''
            
            '''
            # Goal Found

            if next_step == 'goal':
                # final_path.append(goal_cell)
                return final_path

            print(start_cell.get_xy(), '->', goal_cell.get_xy())

            # print_cell_type(explored_grid, n)
            # max_cell = get_max(start_cell, explored_grid, n, i)
            # print(max_cell.get_xy(), start)

            # If we have start cell as goal cell examine again
            if goal_cell == start_cell:
                print("Goal in start cell", goal_cell.get_pg())
                next_step, goal_cell = examine(start_cell, explored_grid, self.type)
                continue

            reset_astar_param(explored_grid)
            path = a_star(explored_grid, start_cell, goal_cell)

            # No path from start to probable goal that means probable goal is not the goal
            if len(path) == 0:
                print("No path found")
                oldpg = goal_cell.get_pg()
                goal_cell.set_pg(0)
                update_prob(explored_grid, goal_cell, oldpg, self.type)
                next_step, goal_cell = examine(start_cell, explored_grid, self.type)
                # final_path = []
                # return final_path
                continue

            path.insert(0, start_cell)
            # print("Path")
            # print_full_path(path)
            for i in range(1, len(path)):
                cell = path[i]
                if cell not in examined_cells:
                    next_step, max_cell = examine_first(cell, explored_grid, grid, self.type, examined_cells)
                else:
                    next_step, max_cell = examine(cell, explored_grid, self.type)
                # print(next_step, cell.get_xy())
                # Block Found Start Cell changed to it's parent
                if next_step == 'block':
                    print('Blocked  :', cell.get_xy())
                    # path[i-1] is examined and we are reexamining at start state again
                    start_cell = path[i-1]
                    # goal_cell = start_cell
                    break

                # Goal Found Exit Agent
                if next_step == 'goal':
                    final_path.append(cell)
                    return final_path

                start_cell = cell
                final_path.append(cell)
                if self.type == 6:
                    if max_cell.get_pg() > goal_cell.get_pg() or (
                            max_cell.get_pg() == goal_cell.get_pg() and check_dist(cell, max_cell) < check_dist(cell,
                                                                                                                goal_cell)):
                        print(cell.get_xy(), ' ', goal_cell.get_xy(), ' ', max_cell.get_xy())
                        break

                if self.type == 7:
                    if max_cell.get_pfg() > goal_cell.get_pfg() or (
                            max_cell.get_pfg() == goal_cell.get_pfg() and check_dist(cell, max_cell) < check_dist(cell,
                                                                                                                  goal_cell)):
                        print(cell.get_xy(), ' ',  goal_cell.get_xy(), ' ', max_cell.get_xy())
                        break
            goal_cell = max_cell


'''
                if self.type == 6:
                    if max_cell.get_pg() > goal_cell.get_pg() or (max_cell.get_pg() == goal_cell.get_pg() and check_dist(cell, max_cell) < check_dist(cell, goal_cell)):
                        break

                if self.type == 7:
                    if max_cell.get_pfg() > goal_cell.get_pfg() or (max_cell.get_pfg() == goal_cell.get_pfg() and check_dist(cell, max_cell) < check_dist(cell, goal_cell)):
                        break
'''

