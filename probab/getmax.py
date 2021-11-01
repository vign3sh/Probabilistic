
def get_max(cell, exp_grid, n, Agent):
    max_cell = set(exp_grid[0][0])
    for i in range(n):
        for j in range(n):
            if Agent == 6:
                if exp_grid[i][j].get_pf() > max_cell[-1].get_pf():
                    max_cell.clear()
                    max_cell.add(exp_grid[i][j])
                elif exp_grid[i][j].get_pf() == max_cell[-1].get_pf() and not(i == 0 and j == 0):
                    dist=check_distance(cell, exp_grid[i][j], max_cell[-1])
                    if dist > 0 :

                    max_cell.add(exp_grid[i][j])


    if(len(ma))
