from tkinter import *
from tkinter import ttk
from GUI_factory import Category_UI
from Lifepath import Lifepath
class GUI_Lifepath(Category_UI):
    """description of class"""
    def __init__(self, master, controller):
        super().__init__(master, controller, frametext='Lifepath', first_header='Years', second_header='Events', third_header='Description')
        self.l = Lifepath()
        #self.l.init_lifepath(16)
        #self.generate_years()
        self.category_int = 0
        self.button_add.destroy()
        self.button_add = ttk.Button(self.frame, text='Add', command=self.add_event)
        self.button_add.grid(column = 0, row = 2, sticky=(W))
        self.text_inventory.destroy()
        self.f4.destroy()
        controller.datasets['lifepath'] = self.l.lifepath_years
        controller.recalculate_points()
        self.starting_year=15

    
    def init_years(self):
        age = int(self.contr.datasets['age'].get())
        self.l.init_lifepath(age)
        self.generate_years()
    def generate_years(self, starting_year=15):
        years = []
        for i in range(len(self.l.lifepath)):
            if i>=starting_year:
                years.append(i)
        self.populate_box(self.box_categories, years )

    def add_event(self):
        try:
            id = self.box_categories.curselection()
            luku = int(id[0])
        except Exception:
            luku = self.category_int
        self.l.add_random_event(luku+self.starting_year)
        key = self.l.lifepath[luku+self.starting_year][0][0]
        #self.categories_and_items[key] = luku
        self.show_list()

    def show_list(self, *args):
        self.box_list.delete(0, END)
        try:
            id = self.box_categories.curselection()
            luku = int(id[0])
            luku = luku + 15
        except Exception:
            luku = self.category_int +15
        self.category_int=luku
        #print('trololo')
        for i in range(len(self.l.lifepath)):
            if i==luku:
                for item in self.l.lifepath[i]:
                    self.box_list.insert(END, item[1])
            
    def show_text(self, *args):
        try:
            id = self.box_list.curselection()
            luku = int(id[0])
        except Exception:
            luku = self.last_list_selection
        year = self.category_int
        self.text_description.delete(1.0, 'end')
        story = ""
        #print(self.l.lifepath[year])
        for text in self.l.lifepath[year][luku]:
            story = story + " " + str(text)
        story = story[3:]
        self.text_description.insert(1.0, story)
        