'''
flat   : terrain = 1
hill   : terrain = 2
forest : terrain = 3
'''


class Cell:

    def __init__(self, x, y, terrain, pf, pg):
        self.terrain = terrain
        self.isTarget = False
        # True Positive
        self.Pf = pf
        self.Pg = pg
        # self.Pfg = self.Pg * self.Pf
        self.X = x
        self.Y = y

    def get_xy(self):
        return self.X, self.Y

    def set_pf(self, pf):
        self.Pf = pf

    def get_pf(self):
        return self.Pf

    def set_pg(self, pg):
        self.Pg = pg

    def get_pg(self):
        return self.Pg

    def get_pfg(self):
        return self.Pf*self.Pg

    def get_target(self):
        return self.isTarget

    def set_target(self):
        self.isTarget = True

    def get_terrain(self):
        return self.terrain

    def set_terrain(self, ter):
        self.terrain = ter

    def __eq__(self, state):
        return self.X == state.x and self.Y == state.y

    def __contains__(self, item):
        return self.X == item.x and self.Y == item.y

    def __hash__(self):
        return hash(self.X + "_" + self.Y)

    def __lt__(self, nxt):
        if isinstance(nxt, Cell):
            return self.Pg < nxt.Pg
        return -1