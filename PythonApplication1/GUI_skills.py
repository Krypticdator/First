from tkinter import *
from tkinter import ttk
from GUI_factory import Category_UI
class GUI_skills(Category_UI):
    """description of class"""
    def __init__(self, master, controller):
        super().__init__(master, controller, frametext='Skills', first_header='Categories', second_header='Skill list', third_header='Description')
        self.set_dictionaries('source/skill_categories.txt','source/skill_descriptions.txt')
        categories = self.collect_categories()
        self.populate_box(self.box_categories, categories)
        

        
    def Assign(self, master, controller):
        '''self.contr = controller
        self.skills_frame = ttk.Labelframe(master, text='Skills')

        
        p = ttk.Panedwindow(self.skills_frame, orient=HORIZONTAL)
        p2 = ttk.Panedwindow(self.skills_frame, orient = HORIZONTAL)

        # first pane, which would get widgets gridded into it:
        f1 = ttk.Labelframe(p, text='Categories', width=100, height=100)
        f2 = ttk.Labelframe(p, text='Skill list', width=100, height=100)
        f3 = ttk.Labelframe(p, text='Description', width=100, height = 100)
        f4 = ttk.LabelFrame(p, text='Actions', width = 100, height = 100)
        p.add(f1)
        p.add(f2)
        p.add(f3)
        p.add(f4)

        f5 = ttk.LabelFrame(p2, text='Your skills', width = 100, height = 100)
        f6 = ttk.LabelFrame(p2, text='Modify', width = 100, height = 100)

        p2.add(f5)
        p2.add(f6)

        lvl_var = StringVar()
        self.spin_lvl = Spinbox(f4, from_=0.0, to=10, textvariable = lvl_var, width = 2)
        lbl_lvl = ttk.Label(f4, text='Lvl')

        self.box_skill_categories = Listbox(f1, height=10, width=25)
        self.box_skill_list = Listbox(f2, height=10, width=25)
        self.box_owned_skills = Listbox(f5, height = 10, width=25)

        self.box_owned_skills.selection_set(0)

        self.button_add = ttk.Button(f4, text = 'Add', command = self.add_skill)
        self.button_buy = ttk.Button(f4, text = 'Buy')
        self.button_delete = ttk.Button(f6, text = 'Delete', command = self.delete_skill)
        

        self.description = Text(f3, width=40, height=10, wrap = 'word')

        s1 = ttk.Scrollbar(f2, orient=VERTICAL, command=self.box_skill_list.yview)
        s2 = ttk.Scrollbar(f3, orient=VERTICAL, command=self.description.yview)

        self.box_skill_list['yscrollcommand'] = s1.set
        self.description['yscrollcommand'] = s2.set
        
        self.skill_cat_dict = {}
        self.skill_categories = self.set_skill_categories()
        self.skill_descriptions = {}
        self.set_skill_descr()
        

        for string in self.skill_categories:
            self.box_skill_categories.insert(END, string)
        self.box_skill_categories.selection_set(0)
        
        self.box_skill_categories.bind('<<ListboxSelect>>', self.show_skills)
        self.box_skill_list.bind('<<ListboxSelect>>', self.show_skill_details)

        p.grid(column = 0, row = 0)
        p2.grid(column = 0, row = 1)
        self.box_skill_categories.grid(column = 0, row = 0)
        self.box_skill_list.grid(column = 0, row = 0)
        s1.grid(column = 1, row = 0, sticky=(N,S))
        self.description.grid(column = 0, row = 0)
        s2.grid(column = 1, row = 0, sticky = (N, S))
        lbl_lvl.grid(column = 0, row = 0)
        self.spin_lvl.grid(column = 1, row = 0)
        self.button_add.grid(column = 0, row = 1, columnspan = 2)
        self.button_buy.grid(column = 0, row = 2, columnspan = 2)
        self.box_owned_skills.grid(column = 0, row = 0)
        self.button_delete.grid(column = 0, row = 0)

        return self.skills_frame'''
        '''
    def set_skill_categories(self):
        categories = []
        self.skill_cat_dict = {}
        d = open('source/skill_categories.txt', 'r')
        for line in d:
            merkkijono = line[:-1]
            rivitiedot = merkkijono.split(";", -1)
            #print(rivitiedot[0])
            self.skill_cat_dict[rivitiedot[1]] = rivitiedot[0]
            if rivitiedot[0] in categories:
                pass
            else:
                #print("False")
                categories.append(rivitiedot[0])
        d.close()
        return categories

    def set_skill_descr(self):
        description = {}
        f = open('source/skill_descriptions.txt', 'r')
        for line in f:
            merkkijono = line[:-1]
            rivitiedot = merkkijono.split(";", -1)
            #print(rivitiedot)
            self.skill_descriptions[rivitiedot[0]] = rivitiedot[1]
        f.close()
   
    def show_skills(self, *args):
        self.box_skill_list.delete(0, END)
        id = self.box_skill_categories.curselection()
        luku = int(id[0])

        if luku == 0:
            for avain, arvo in self.skill_cat_dict.items():
                if arvo == "Fighting":
                    self.box_skill_list.insert(END, avain)
        if luku == 1:
            for avain, arvo in self.skill_cat_dict.items():
                if arvo == "Ranged Weapons":
                    self.box_skill_list.insert(END, avain)
        if luku == 2:
            for avain, arvo in self.skill_cat_dict.items():
                if arvo == "Awarness":
                    self.box_skill_list.insert(END, avain)
        if luku == 3:
            for avain, arvo in self.skill_cat_dict.items():
                if arvo == "Control":
                    self.box_skill_list.insert(END, avain)
        if luku == 4:
            for avain, arvo in self.skill_cat_dict.items():
                if arvo == "Body":
                    self.box_skill_list.insert(END, avain)
        if luku == 5:
            for avain, arvo in self.skill_cat_dict.items():
                if arvo == "Interaction":
                    self.box_skill_list.insert(END, avain)
        if luku == 6:
            for avain, arvo in self.skill_cat_dict.items():
                if arvo == "Technique":
                    self.box_skill_list.insert(END, avain)
        if luku == 7:
            for avain, arvo in self.skill_cat_dict.items():
                if arvo == "Performance":
                    self.box_skill_list.insert(END, avain)
        if luku == 8:
            for avain, arvo in self.skill_cat_dict.items():
                if arvo == "Education":
                    self.box_skill_list.insert(END, avain)

    def show_skill_details(self, *args):
        id = self.box_skill_list.curselection()
        luku = int(id[0])
        self.description.delete(1.0, 'end')
        text = self.skill_descriptions[self.box_skill_list.get(luku)]
        self.description.insert(1.0, text)

    def add_skill(self):
        id = self.box_skill_list.curselection()
        luku = int(id[0])
        skill = self.box_skill_list.get(luku)

        lvl = int(self.spin_lvl.get())
        self.contr.setChar_skill(skill, lvl)
        self.update_player_skills()
    
    def update_player_skills(self):
        self.box_owned_skills.delete(0,END)
        skill_list = self.contr.get_char_skill_dictionary()
        
        for skill, lvl in skill_list.items():
            if lvl != 0:
                merkkijono = skill + " " + str(lvl)
                self.box_owned_skills.insert(END, merkkijono)

    def delete_skill(self):
        id = self.box_owned_skills.curselection()
        luku = int(id[0])
        merkkijono = self.box_skill_list.get(luku)
        print(merkkijono)
        skill = merkkijono[:-2]
        print(skill)
        

        '''
