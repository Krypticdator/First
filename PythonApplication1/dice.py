from random import randrange


class Dice:
    def __init__(self, num=1, sides=6):
        self.__last_roll = 0
        self.__num = num
        self.__sides = sides
        self.__rolls = []
        self.__dice = 0

    def roll(self, num=3, sides=6):
        self.__last_roll = sum(randrange(sides) + 1 for die in range(num))
        self.__rolls.append(self.__last_roll)
        return self.__last_roll

    def Roll(self, num=3, sides=6):
        self.__last_roll = sum(randrange(sides) + 1 for die in range(num))
        self.__rolls.append(self.__last_roll)
        return self.__last_roll





	
			
			
       



    
