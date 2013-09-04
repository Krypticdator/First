from Character import Character
from Settings import Settings
from Fuzion import Fuzion

class Controller():
    """description of class"""
    def __init__(self):
        self.__char = Character()
        #self.__char.setRandomStats()
        self.settings = Settings()

    def getChar_stats(self):
        return self.__char_get_attributes()

    def get_Wpn_availability(self):
        return self.__char.getAttributeRoll("Luck")

    def getChar_stat(self, stat):
        return self.__char.get_attribute(stat)

    def setChar_stat(self, stat, value):
        self.__char.set_attribute(stat, value)

    def clear_all_skills(self):
        list = self.__char.get_skills()

        for key, value in list.items():
            list[key] = 0

    def set_char_skill(self, skill, value):
        self.__char.add_skill(skill, value)

    def get_char_skill_dictionary(self):
        return self.__char.get_skills()

    def clear_ability_list(self, name):
        list = self.__char.get_ability_list(name)

        for key, value in list.items():
            list[key] = 0

    def set_to_ability_list(self, list, ability, value):
        self.__char.set_to_ability_list(list, ability, value)

    def print_all_abilities(self):
        for key, dictionary in self.__char.all_abilities.items():
            for key2, value in dictionary.items():
                if value!=0:
                    print(key2 + ' ' + value)

    def get_char_skill(self, skill):
        return self.__char.get_skill(skill)

    def get_r_name(self, nametype, gender="Male"):
        x = Character()
        x.giveRandomName(gender)

        if nametype == "first":
            return x.get_attribute("First name")
        if nametype == "second":
            return x.get_attribute("Second name")
        if nametype == "last":
            return x.get_attribute("Last name")
        if nametype == "nick":
            return x.get_attribute("First alias") + x.get_attribute("Last alias")
