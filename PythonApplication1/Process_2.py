from item import item
from Character import Character
import math

class Process_2(object):
    """description of class"""
    def __init__(self):
        self.__req_skills = []
        self.__skill_performances = {}
        self.__req_input_items = []
        self.__items = {}
        self.__output_item = item()

    def add_req_skill(self, skill):
        self.__req_skills.append(skill)
        self.__skill_performances[skill] = 0

    def add_req_input_item(self, item_type):
        self.__req_input_items.append(item_type)

    def set_output_item_name(self, name):
        self.__output_item.set_attribute("name", name)

    def perform_skill(self, skill, character):
        skill_throw = character.get_skill_throw(skill)
        if skill in self.__req_skills:
            self.__skill_performances[skill] = skill_throw

    def addItem(self, item):
        if item.get_attribute("type") in self.__req_input_items:
            self.__items[item.get_attribute("type")] = item
            self.__output_item.add_linked_item(item)

    def is_ready(self):
        done = 0
        reqs = len(self.__req_input_items) + len(self.__req_skills)
        
        try:
            for i in range(0, len(self.__req_input_items)):
                if self.__req_input_items[i] in self.__items:
                    done += 1
        except Exception:
            pass
        
        try:
            for key, value in self.__skill_performances.items():
                if value != 0:
                    done += 1
        except Exception:
            pass

        if done == reqs:
            item_performance = []
            skill_performance = []

            try:
                for key, value in self.__skill_performances.items():
                    skill_performance.append(value)
            except Exception:
                pass

            try:
                for key, value in self.__items.items():
                    item_performance.append(value.get_attribute("quality"))
            except Exception:
                pass

            divide = len(item_performance) + len(skill_performance)
            total = sum(item_performance) + sum(skill_performance)
            try:
                result = total / divide
            except Exception:
                result = total
            self.__output_item.set_attribute("quality", result)

            


