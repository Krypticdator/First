from tkinter import *
from tkinter import ttk
from GUI_factory import Category_UI
from Lifepath import Lifepath
class GUI_Lifepath(Category_UI):
    """description of class"""
    def __init__(self, master, controller):
        super().__init__(master, controller, frametext='Lifepath', first_header='Years', second_header='Events', third_header='Description')
        self.l = Lifepath()
        self.l.init_lifepath(16)
        self.generate_years()
        self.category_int = 0
        self.button_add.destroy()
        self.button_add = ttk.Button(self.frame, text='Add', command=self.add_event)
        self.button_add.grid(column = 0, row = 1, sticky=(W))
        self.text_inventory.destroy()
        self.f4.destroy()


    def generate_years(self):
        years = []
        for i in range(len(self.l.lifepath)):
            years.append(i)
        self.populate_box(self.box_categories, years )

    def add_event(self):
        try:
            id = self.box_categories.curselection()
            luku = int(id[0])
        except Exception:
            luku = self.category_int
        self.l.add_random_event(luku)
        key = self.l.lifepath[luku][0][0]
        #self.categories_and_items[key] = luku
        self.show_list()

    def show_list(self, *args):
        self.box_list.delete(0, END)
        try:
            id = self.box_categories.curselection()
            luku = int(id[0])
        except Exception:
            luku = self.category_int
        self.category_int=luku
        #print('trololo')
        for i in range(len(self.l.lifepath)):
            if i==luku:
                for item in self.l.lifepath[i]:
                    self.box_list.insert(END, item[1])
            
    def show_text(self, *args):
        id = self.box_list.curselection()
        luku = int(id[0])
        year = self.category_int
        self.text_description.delete(1.0, 'end')
        story = ""
        print(self.l.lifepath[year])
        for text in self.l.lifepath[year][luku]:
            story = story + " " + str(text)
        story = story[3:]
        self.text_description.insert(1.0, story)
        