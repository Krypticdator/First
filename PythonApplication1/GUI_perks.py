from tkinter import *
from tkinter import ttk
from GUI_factory import Category_UI

class GUI_perks(Category_UI):
    """description of class"""
    def __init__(self, master, controller):
        super().__init__(master, controller, frametext='Perks', first_header='Not used', second_header='Perks', third_header='Description')
        self.f1.destroy()
        self.perks = []
        self.populate_box(self.box_list, self.perks, 'source/perks.txt')
        self.set_dictionaries(filepath_descriptions='source/perk_descriptions.txt', sep='_')


        