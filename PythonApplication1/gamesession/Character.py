from GameObject import GameObject
class Character(GameObject):
    """description of class"""

    def __init__(self):
        super().__init__()

    def load(self):
        pass

    def save(self):
        pass

class Stat(GameObject):
    def __init__(self, name='undefined', type='skill', stat='int', lvl=0, ip=0, diff=1, chip=False, frequency=0, importance=0, intensity=0, original=0):
        super().__init__()
        self.set_attribute('name', name)
        self.set_attribute('type', type)
        self.set_attribute('lvl', lvl)
        if type=='skill':
            self.set_attribute('stat', stat)
            self.set_attribute('ip', ip)
            self.set_attribute('diff',diff)
            self.set_attribute('chip', chip)
        elif type=='complication':
            self.set_attribute('frequency', frequency)
            self.set_attribute('importance', importance)
            self.set_attribute('importance', importance)
        elif type=='stat':
            self.set_attribute('original', original)

    def increase_experience(self, exp):
        pool = self.get_attribute('ip')
        lvl = self.get_attribute('lvl')
        diff_mod = self.get_attribute('diff')
        cp_mod=1 #Kuinka nopeasti tasot kasvavat
        pool += exp

        while pool>(lvl*diff_mod*cp_mod):
            limit = (lvl +1) * diff_mod * cp_mod
            pool -=limit
            lvl = lvl +1

        self.set_attribute('lvl',lvl)
        self.set_attribute('ip',pool)


class Effect(GameObject):
    def __init__(self, name='default', duration='forever', modifier=0, target_type='stat', target_name='int'):
        super().__init__()
        self.set_attribute('name', name)
        self.set_attribute('duration', duration)
        self.set_attribute('modifier', modifier)
        self.set_attribute('target_type', target_type)
        self.set_attribute('target_name', target_name)
        


