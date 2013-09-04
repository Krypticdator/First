from tkinter import *
from tkinter import ttk
from GUI_factory import Category_UI
class GUI_complications(Category_UI):
    """description of class"""
    def __init__(self, master, controller):
        super().__init__(master, controller, frametext='Complications', first_header='Categories', second_header='Complications', third_header='Description')
        self.set_dictionaries('source/complication_categories.txt','source/complications_descriptions.txt')
        categories = self.collect_categories()
        self.populate_box(self.box_categories, categories)

    def Assign(self, master, controller):
        '''self.contr = controller
        self.com_frame = ttk.Labelframe(master, text='Complications')

        
        p = ttk.Panedwindow(self.com_frame, orient=HORIZONTAL)
        p2 = ttk.Panedwindow(self.com_frame, orient = HORIZONTAL)

        # first pane, which would get widgets gridded into it:
        f1 = ttk.Labelframe(p, text='Categories', width=100, height=100)
        f2 = ttk.Labelframe(p, text='Complications', width=100, height=100)
        f3 = ttk.Labelframe(p, text='Description', width=100, height = 100)
        f4 = ttk.Labelframe(p2, text='Frequency', width=100, height = 100)
        f5 = ttk.Labelframe(p2, text='Intensity', width=100, height = 100)
        f6 = ttk.Labelframe(p2, text='Importance', width=100, height = 100)

        p.add(f1)
        p.add(f2)
        p.add(f3)

        p2.add(f4)
        p2.add(f5)
        p2.add(f6)

        self.box_com_categories = Listbox(f1, height=10, width=25)
        self.box_com_list = Listbox(f2, height=10, width=25)

        frequency = StringVar()
        intensity = StringVar()
        importance = StringVar()
        freq1 = ttk.Radiobutton(f4, text='Infrequently(5): Once every few gaming sessions', variable=frequency, value=5)
        freq2 = ttk.Radiobutton(f4, text='Frequently(10): Once every gaming session', variable=frequency, value=10)
        freq3 = ttk.Radiobutton(f4, text='Constantly(15): More than once every gaming session', variable=frequency, value=15)

        inten1 = ttk.Radiobutton(f5, text='Mild (5)', variable=intensity, value=5)
        inten2 = ttk.Radiobutton(f5, text='Strong (10)', variable=intensity, value=10)
        inten3 = ttk.Radiobutton(f5, text='Severe(15)', variable=intensity, value=15)
        inten4 = ttk.Radiobutton(f5, text='Extreme(20)', variable=intensity, value=20)

        impor1 = ttk.Radiobutton(f6, text='Minor', variable=importance, value=5)
        impor2 = ttk.Radiobutton(f6, text='Major', variable=importance, value=2)
        impor3 = ttk.Radiobutton(f6, text='Extreme', variable=importance, value=1)

        self.description = Text(f3, width=40, height=10, wrap = 'word')

        s1 = ttk.Scrollbar(f2, orient=VERTICAL, command=self.box_com_list.yview)
        s2 = ttk.Scrollbar(f3, orient=VERTICAL, command=self.description.yview)

        self.box_com_list['yscrollcommand'] = s1.set
        self.description['yscrollcommand'] = s2.set

        self.com_category_dict = {}
        self.com_categories = self.set_com_categories()
        self.com_descriptions = {}
        self.set_com_descr()

        for string in self.com_categories:
            self.box_com_categories.insert(END, string)
        self.box_com_categories.selection_set(0)
        
        self.box_com_categories.bind('<<ListboxSelect>>', self.show_coms)
        self.box_com_list.bind('<<ListboxSelect>>', self.show_com_details)

        p.grid(column = 0, row = 0)
        p2.grid(column = 0, row = 1)
        self.box_com_categories.grid(column = 0, row = 0)
        self.box_com_list.grid(column = 0, row = 0)
        s1.grid(column = 1, row = 0, sticky=(N,S))
        self.description.grid(column = 0, row = 0)
        s2.grid(column = 1, row = 0, sticky = (N, S))
        freq1.grid(column = 0, row = 0, sticky = (W))
        freq2.grid(column = 0, row = 1, sticky = (W))
        freq3.grid(column = 0, row = 2, sticky = (W))
        inten1.grid(column = 0, row = 0, sticky = (W))
        inten2.grid(column = 0, row = 1, sticky = (W))
        inten3.grid(column = 0, row = 2, sticky = (W))
        inten4.grid(column = 0, row = 3, sticky = (W))
        impor1.grid(column = 0, row = 0, sticky = (W))
        impor2.grid(column = 0, row = 1, sticky = (W))
        impor3.grid(column = 0, row = 2, sticky = (W))

        return self.com_frame'''
'''
    def set_com_categories(self):
        categories = []
        d = open('source/complication_categories.txt', 'r')
        for line in d:
            merkkijono = line[:-1]
            rivitiedot = merkkijono.split(";", -1)
            #print(rivitiedot[0])
            self.com_category_dict[rivitiedot[1]] = rivitiedot[0]
            if rivitiedot[0] in categories:
                pass
            else:
                #print("False")
                categories.append(rivitiedot[0])
        d.close()
        return categories

    def set_com_descr(self):
        description = {}
        f = open('source/complications_descriptions.txt', 'r')
        for line in f:
            merkkijono = line[:-1]
            rivitiedot = merkkijono.split(";", -1)
            #print(rivitiedot)
            self.com_descriptions[rivitiedot[0]] = rivitiedot[1]
        f.close()
   
    def show_coms(self, *args):
        self.box_com_list.delete(0, END)
        id = self.box_com_categories.curselection()
        luku = int(id[0])

        if luku == 0:
            for avain, arvo in self.com_category_dict.items():
                if arvo == "Psychological Complications":
                    self.box_com_list.insert(END, avain)
        if luku == 1:
            for avain, arvo in self.com_category_dict.items():
                if arvo == "Personality Traits":
                    self.box_com_list.insert(END, avain)
        if luku == 2:
            for avain, arvo in self.com_category_dict.items():
                if arvo == "Physiological Limitations":
                    self.box_com_list.insert(END, avain)
        if luku == 3:
            for avain, arvo in self.com_category_dict.items():
                if arvo == "Social Complications":
                    self.box_com_list.insert(END, avain)
        if luku == 4:
            for avain, arvo in self.com_category_dict.items():
                if arvo == "Responsibilities":
                    self.box_com_list.insert(END, avain)
        if luku == 5:
            for avain, arvo in self.com_category_dict.items():
                if arvo == "Compulsive Behaviors":
                    self.box_com_list.insert(END, avain)

    def show_com_details(self, *args):
        id = self.box_com_list.curselection()
        luku = int(id[0])
        self.description.delete(1.0, 'end')
        text = self.com_descriptions[self.box_com_list.get(luku)]
        self.description.insert(1.0, text)

   '''
        

        
