from tkinter import *
from tkinter import ttk
from GUI_factory import Category_UI

class GUI_talents(Category_UI):
    """description of class"""
    def __init__(self, master, controller):
        super().__init__(master, controller, frametext='Talents', first_header='Not used', second_header='Talents', third_header='Description')
        self.f1.destroy()
        talents = []
        self.populate_box(self.box_list, talents, 'source/talents.txt')
        self.set_dictionaries(filepath_descriptions = 'source/talent_descriptions.txt',sep='_')

   