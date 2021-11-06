'''
flat   : terrain = 1
hill   : terrain = 2
forest : terrain = 3
'''


class Cell:

    def __init__(self, x, y, terrain, pf, pg, parent=None):
        self.terrain = terrain
        self.isTarget = False
        # True Positive
        self.Pf = pf
        self.Pg = pg
        # self.Pfg = self.Pg * self.Pf
        self.X = x
        self.Y = y
        self.parent = parent
        self.gx = 0

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
        return self.X == state.X and self.Y == state.Y

    def __contains__(self, item):
        return self.X == item.X and self.Y == item.Y

    def __hash__(self):
        return hash(str(self.X) + "_" + str(self.Y))

    def get_parent(self):
        return self.parent

    def set_parent(self, cell):
        self.parent = cell

    def set_gx(self, gx):
        self.gx = gx

    def get_gx(self):
        return self.gx
