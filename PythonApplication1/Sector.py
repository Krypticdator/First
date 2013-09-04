from Character import Character

class Sector(object):
    """description of class"""
    def __init__(self):
        self.__population = []
        self.__groups = []

    def populate(self, amount):
        for i in range(0, amount):
            x = Character()
            x.setRandomSkills()
            x.setRandomStats()
            self.__population.append(x)

