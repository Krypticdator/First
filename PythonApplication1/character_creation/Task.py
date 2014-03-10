from Fuzion import Fuzion

class Task(object):
    """description of class"""

    def __init__(self):
        self.__Challenger ="" #Character()
        self.__Target = ""#Character()
        self.__Challenger_attribute = ""
        self.__Challenger_attribute_t = 0
        self.__Challenger_skill = ""
        self.__Challenger_skill_t = 0
        self.__Target_attribute = ""
        self.__Target_attribute_t = 0
        self.__Target_skill = ""
        self.__Target_skill_t = 0
        self.__margin_of_succ_or_failure = 0
        self.__fuzion = Fuzion()

    def Q_race(self, Challenger, Target, c_skill, t_skill): #Challenger tries to win targets skill with own skill
        self.__Challenger = Challenger
        self.__Target = Target

        self.__Challenger_skill_t = Challenger.getSkillThrow(c_skill)
        self.__Target_skill_t = Target.getSkillThrow(t_skill)
        self.__margin_of_succ_or_failure = self.__Challenger_skill_t - self.__Target_skill_t
        return self.__margin_of_succ_or_failure
    
    def Q_attribute_race(self, Challenger, Target, c_attribute, t_attribute):
        self.__Challenger = Challenger
        self.__Target = Target

        self.__Challenger_attribute_t = Challenger.getAttributeRoll(c_attribute)
        self.__Target_attribute_t = Target.getAttributeRoll(t_attribute)

        self.__margin_of_succ_or_failure = self.__Challenger_attribute_t - self.__Target_attribute_t
        return self.__margin_of_succ_or_failure
    
    def Run_Custom(self):
        c_roll = self.__Challenger_attribute + self.__Challenger_skill + self.__fuzion.Roll()
        t_roll = self.__Target_attribute + self.__Target_skill + self.__fuzion.Roll()
        self.__margin_of_succ_or_failure = c_roll - t_roll
        return self.__margin_of_succ_or_failure
    
    def set_c_skill(self, skill, Challenger, num = 0):
        if num == 0:
            self.__Challenger_skill = Challenger.get_skill(skill)
        else:
            print("else lausekkeessa")
            self.__Challenger_skill = num

    def set_c_attribute(self, attribute, Challenger, num = 0):
        if num == 0:
            self.__Challenger_attribute = Challenger.get_stat(attribute)
        else:
            print("else lausekkeessa")
            self.__Challenger_attribute = num

    def set_t_skill(self, skill, Target, num = 0):
        if num == 0:
            self.__Target_skill = Target.get_skill(skill)
        else:
            print("else lausekkeessa")
            self.__Target_skill = num

    def set_t_attribute(self, attribute, Target, num = 0):
        if num == 0:
            self.__Target_attribute = Target.get_stat(attribute)
        else:
            print("else lausekkeessa")
            self.__Target_attribute = num


