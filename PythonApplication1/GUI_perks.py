from tkinter import *
from tkinter import ttk
from GUI_factory import Category_UI
from Character import Character

class GUI_perks(Category_UI):
    """description of class"""
    def __init__(self, master, controller):
        super().__init__(master, controller, frametext='Perks', first_header='Not used', second_header='Perks', third_header='Description')
        self.f1.destroy()
        self.perks = []
        self.populate_box(self.box_list, self.perks, 'source/perks.txt')
        self.set_dictionaries(filepath_descriptions='source/perk_descriptions.txt', sep='_')

    def add_to_inventory(self, *args):
        id = self.box_list.curselection()
        luku = int(id[0])
        text = self.box_list.get(luku)
        if text=='Favor' or text=='Contact':
            x = Character()
            x.giveRandomName()
            name = x.get_attribute('Full name')
            text = text + '(' + name + ')'
        self.contr.set_to_ability_list(self.name, text, 1)
        #list = self.contr.get_from_ability_list(self.name)
        #value = self.contr.get_char_skill(text)
        value = self.contr.get_from_ability_list(self.name, text)

        text = text + '\t\t\t\t|' + str(value) + '\n'
        self.text_inventory.insert('end', text)

        