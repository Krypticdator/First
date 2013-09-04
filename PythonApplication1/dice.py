from random import randrange

class Dice:
    __dice = 0

    def Roll(self, num = 3, sides = 6):
        self.__dice = sum(randrange(sides)+1 for die in range(num))
        return self.__dice
       



    
