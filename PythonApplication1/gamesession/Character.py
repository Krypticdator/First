from GameObject import GameObject
class Character(GameObject):
    """description of class"""

    def __init__(self):
        super().__init__()

class Stat(GameObject):
    def __init__(self, type='skill', stat='int', lvl=0, ip=0, diff=1, chip=False):
        super().__init__()
        if type=='skill':
            self.set_attribute('stat', stat)
            self.set_attribute('lvl', lvl)
            self.set_attribute('ip', ip)
            self.set_attribute('diff',diff)
            self.set_attribute('chip', chip)
        if type=='complication':
            self.set_attribute('frequency', frequency)
            self.set_attribute


class Effect(GameObject):
    def __init__(self, name='default', duration='forever', modifier=0, target_type='stat', target_name='int'):
        super().__init__()
        self.set_attribute('name', name)
        self.set_attribute('duration', duration)
        self.set_attribute('modifier', modifier)
        self.set_attribute('target_type', target_type)
        self.set_attribute('target_name', target_name)
        


