from dice import Dice
from random import randrange

class Fuzion(Dice):
    

    def __init__(self):
        self.__c_failure = 3
        self.__c_success = 18
        self.__roll_statistics = []
        self.__last_result = 0
        self.__margin_of_succ_or_fail = 0

    def Rand_method(self, num, sides):
        return sum(randrange(sides)+1 for die in range(num))

    def Roll(self, num = 3, sides = 6):
        self.__dice = self.Rand_method(num, sides)
        
        if self.__dice == self.__c_failure:
            #print("critical failure")
            failure = self.Rand_method(2, 6)
            self.__dice = self.__dice - failure
            #if self.__dice < 0:
            #  self.__dice = 0;
            
        if self.__dice == self.__c_success:
            #print("critical success")
            #print(self.__dice)
            success = self.Rand_method(2, 6)
            #print(success)
            self.__dice = self.__dice + success
            self.__last_result = self.__dice

        self.__roll_statistics.append(self.__dice)
        
        return self.__dice

    def getStatistics(self):
        return self.__roll_statistics

    def analyze_statistics(self):
        for i in range(60):
            a = i
            print(int(a), " = ", int(self.__roll_statistics.count(a)))

