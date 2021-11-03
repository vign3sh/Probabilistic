from probab.examine import *
from probab.utility import *
from probab.astar import a_star


class Agent:

    def __init__(self, number):
        self.type = number

    def agent(self, start_cell, explored_grid, grid, n, examined_cells):
        final_path = [start_cell]
        while True:
            path = []
            if start_cell in examined_cells:
                next_step, goal_cell = examine_first(start_cell, explored_grid, grid, self.type, examined_cells)
            else:
                next_step, goal_cell = examine(start_cell, explored_grid, grid, self.type)


            if next_step == 'goal':
                return final_path

            print(goal_cell.get_xy(), start_cell.get_xy())
            print_ex_grid(explored_grid, n)
            # print_cell_type(explored_grid, n)
            # max_cell = get_max(start_cell, explored_grid, n, i)
            # print(max_cell.get_xy(), start)

            # If we have start cell as goal cell examine again
            if goal_cell.get_xy() == start_cell.get_xy():
                continue

            path = a_star(grid, start_cell, goal_cell)

            # No path from start to probable goal
            if len(path) == 0:
                print("No path found")
                final_path = []
                return final_path

            for i in range(1, len(path)):
                cell = path[i]
                if cell in examined_cells:
                    next_step, max_cell = examine_first(start_cell, explored_grid, grid, self.type, examined_cells)
                else:
                    next_step, max_cell = examine(start_cell, explored_grid, grid, self.type)

                # Goal Found Exit Agent
                if next_step == 'goal':
                    return final_path

                # Block Found Start Cell changed to it's parent
                elif next_step == 'block':
                    start = path[i-1]
                    break

                final_path.append(cell)

            start_cell = goal_cell

