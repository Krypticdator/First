from Character import Character
from item import item
import math

class Process:
    

    def __init__(self):
        self.__req_skills = []
        self.__req_items = {}
        self.__task_group = []
        self.__performance = []
        self.__final_performance = 0 #Output success
        self.__difficulty = 0
        self.__resolution = 0        #Margin of success or failure
        self.__timeresolution = 5      #maximum time for this process in minutes
        self.__output = item()
    

    def assign_to_taskgroup(self, Character):
        self.__task_group.append(Character)
        if self.__req_skills.count == 0:
            pass
        else:
            for i in range(0, len(self.__req_skills)):
                Character.get_skill(self.__req_skills[i])

    def calc_resolution(self):
        self.__resolution = self.__final_performance - self.__difficulty

    def get_resolution(self):
        return self.__resolution
    
    def run_process(self):
        self.__performance.clear()
        print(self.__req_skills)
        try:
            for i in range(0, len(self.__task_group)):
                for a in range(0, len(self.__req_skills)):
                    self.__performance.append(self.__task_group[i].getSkillThrow(self.__req_skills[a]))
        except Exception:
            pass
        
        try:
            for key, value in self.__req_items.items():
                self.__performance.append(int(value))
        except Exception:
            pass
        
        try:    
            divider = len(self.__performance) + len(self.__req_items)
            total = sum(self.__performance)
            self.__final_performance = total/divider
            self.calc_resolution()
        except Exception:
            pass
       
        try:
            self.__output.set_quality(self.__resolution)
        except Exception:
            pass
         
    def set_req_skills(self, skill):
        self.__req_skills.append(skill)
        if self.__task_group.count == 0:
            pass
        else:
            for i in range(len(self.__task_group)):
                self.__task_group[i].get_skill(skill)

    def set_difficulty(self, difficulty):
        self.__difficulty = difficulty

    def get_performance(self):
        print(self.__final_performance)
        return self.__performance