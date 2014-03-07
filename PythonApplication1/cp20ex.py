class cp20ex(object):
    """description of class"""
    def __init__(self, lvl=0, pool=0, diff_mod=1, cp_mod=1):
        self.lvl = lvl
        self.pool = pool
        self.diff_mod = diff_mod
        self.cp_mod = cp_mod

    def increase_experience(self, exp):
        self.pool += exp

        while self.pool>(self.lvl*self.diff_mod*self.cp_mod):
            limit = (self.lvl +1) * self.diff_mod * self.cp_mod
            self.pool -=limit
            self.lvl = self.lvl +1





