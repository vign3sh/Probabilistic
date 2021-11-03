
class Agent:

    def __init__(self):
        self.type = type

    def follow_path(self, explored_grid, path):
        final_state = None

        for state in path:
            self.update_explored_grid(explored_grid, state)

            # if we encounter an block in our path we check for final state and also mark it as blocked
            if self.complete_grid[state.x][state.y] == 1:
                explored_grid[state.x][state.y] = 1
                final_state = state.parent_state
                break

            # if we have found the goal state then also we should return
            if state.x == self.goal_state.x and state.y == self.goal_state.y:
                self.bumped = False
                final_state = state
                break

        return final_state
