from tkinter import *
from tkinter import ttk
from Controller import Controller
from Character import Character
from Process import Process
from Fuzion import Fuzion
from dice import Dice
from Bar_test import Bar
from Character_layout import Character_Layout
from Process_2 import Process_2
from item import item
from Settings import Settings
from GUI_math_analysis import GUI_math_analysis
from Lifepath import Lifepath
from inherited import inherited
from inheritable import inheritable
from GUI_factory import Category_UI
from GUI_Lifepath import GUI_Lifepath
from GUI_item_creator import GUI_item_creator
from xml_control import xml_control
from cp20ex import cp20ex
from Armor import Effective_armor
from Armor import Armor


class start:
    def __init__(self):
        self.root = Tk()
        self.root.title('program')
        self.root.option_add('*tearOff', FALSE)

        menubar = Menu(self.root)
        self.root['menu'] = menubar

        menu_file = Menu(menubar)
        menu_edit = Menu(menubar)
        menubar.add_cascade(menu=menu_file, label='File')
        menubar.add_cascade(menu=menu_edit, label='Tools')
        menu_file.add_command(label='New Character', command=self.newChar)
        menu_edit.add_command(label='Item creator', command = self.newItem)
        menu_edit.add_command(label='Probabilities', command = self.probabs)
        menu_edit.add_command(label='Combat probabilities', command=self.combat_probabs)
        self.root.mainloop()

        file = xml_control()
        
        

    def newChar(self):
        window = Toplevel(self.root)
        self.layout = Character_Layout(window)
        #print(self.layout.contr.datasets)
    def newItem(self):
        window = Toplevel(self.root)
        toolswindow = GUI_item_creator(window)
    def probabs(self):
        probs = GUI_math_analysis()
        window = Toplevel(self.root)
        probs.assign('none', window, self.root)
    def combat_probabs(self):
        pass

x = start()
cp= cp20ex()
contr = Controller()
a1 = contr.settings.armors[0]
a2 = contr.settings.armors[1]
a3 = contr.settings.armors[2]
e = Effective_armor()


    

#x = Character()
#y = Process()
#z = Fuzion()
#b = Bar()
#layout = Character_Layout()

#b.Operate_hour()

#x = Character()
#y = Character()
#p = Process_2()
#i = item()
#s = Settings()
'''contr = Controller()
root = Tk()
content = ttk.Frame(root)

x = GUI_math_analysis()
x.assign(contr, content, root)

content.grid(column=0, row=0)
root.mainloop()'''



